"""
Emerging Issues API
--------------------
Clusters existing complaints WITHIN each category (Electrical, Maintenance,
Plumbing, Security) using sentence embeddings, labels clusters via TF-IDF
keywords, and exposes clusters of size >= MIN_CLUSTER_SIZE as "emerging
issues" cards for the admin dashboard. Each result includes the list of
complaint IDs in that cluster, so the frontend can pull the actual complaint
rows out of whatever list it already has (no separate fetch needed, and any
status/assign change made elsewhere is automatically reflected here too).

Clustering algorithm: AgglomerativeClustering with cosine distance, not
HDBSCAN. HDBSCAN is density-based and has a "noise" concept (points that
don't get assigned to any cluster) -- that works great on large, messy,
real-world data, but is notoriously unreliable on small sample sizes in
high-dimensional embedding spaces (this model produces 384-dim vectors),
where distance/density estimates get unstable. AgglomerativeClustering
with a fixed distance_threshold has no noise concept at all -- every point
is assigned to some cluster -- which sidesteps that whole failure mode.
The >= MIN_CLUSTER_SIZE business rule is then applied afterwards, as a
simple filter on cluster size, same as before.

Results are cached in-memory per society with a TTL so we don't
re-embed/re-cluster on every request.
"""

import time
from collections import defaultdict

from flask import Blueprint, current_app

from app.api.utils import current_user
from app.core.responses import fail, ok
from app.core.security import ROLE_ADMIN, roles_required
from app.models import Complaint

emerging_issues_bp = Blueprint("emerging_issues", __name__, url_prefix="/complaints/emerging")

MIN_CLUSTER_SIZE = 5
CACHE_TTL_SECONDS = 300  # recompute at most every 5 minutes per society

# Cosine DISTANCE threshold (0 = identical, 2 = opposite; 1 = unrelated/orthogonal).
# Two complaints merge into the same cluster if their embeddings are within this
# distance of each other. Lower = stricter (only near-duplicates merge). This is
# the one knob to tune based on real similarity numbers from the /debug route.
DISTANCE_THRESHOLD = 0.5

# in-memory cache: {society_id: {"data": [...], "ts": float}}
_cache = {}

_model = None  # lazy-loaded SentenceTransformer, shared across requests


def _get_model():
    """Load the sentence-transformer model once and reuse it for every request.
    device="cpu" is passed explicitly (rather than left to auto-detection) as a
    defensive measure against a known PyTorch/transformers compatibility issue
    where newer transformers versions can leave model weights on a placeholder
    "meta" device; forcing an explicit device sidesteps that lazy-loading path."""
    global _model
    if _model is None:
        from sentence_transformers import SentenceTransformer
        _model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")
    return _model


def _embed(texts):
    model = _get_model()
    return model.encode(texts, show_progress_bar=False, normalize_embeddings=True)


def _rank_by_centrality(idxs, embeddings):
    """Ranks cluster member indices by how "central"/representative they are
    (highest average similarity to every other member), most central first.
    Shared by both the medoid title fallback and the sampling used for
    generation, so both pick genuinely typical complaints rather than an
    arbitrary or idiosyncratic subset."""
    import numpy as np

    cluster_embeddings = embeddings[idxs]
    # embeddings are L2-normalized, so a dot product here is the same as cosine similarity
    similarity_matrix = cluster_embeddings @ cluster_embeddings.T
    total_similarity = similarity_matrix.sum(axis=1)
    order = np.argsort(-total_similarity)  # descending: most central first
    return [idxs[i] for i in order]


def _representative_subject(complaints, idxs, embeddings):
    """Picks the most "central" complaint in a cluster (the one most similar,
    on average, to every other complaint in that cluster) and returns its real
    subject line as the card title. Used as a fallback if title generation
    below is unavailable or fails for any reason."""
    ranked = _rank_by_centrality(idxs, embeddings)
    return complaints[ranked[0]].subject


_title_generator = None  # lazy-loaded FLAN-T5 pipeline, shared across requests


def _get_title_generator():
    """Loads a small, free, local text-generation model (google/flan-t5-small,
    Apache 2.0 licensed) once and reuses it. Runs entirely offline after the
    first download -- no API key, no per-call cost. This is used to generate a
    genuinely new short title for a cluster (not lifted verbatim from any one
    complaint).

    device="cpu" and low_cpu_mem_usage=False are both set explicitly for the
    same reason as in _get_model(): newer transformers can lazily load weights
    onto a placeholder "meta" device (accelerate's low-memory loading path),
    which has been seen to leave global loading state altered in a way that
    then breaks the *next* model loaded in the same process -- including,
    confusingly, the unrelated sentence-transformer model above. Disabling
    that path here avoids the whole class of problem."""
    global _title_generator
    if _title_generator is None:
        from transformers import pipeline
        _title_generator = pipeline(
            "text2text-generation",
            model="google/flan-t5-small",
            device="cpu",
            model_kwargs={"low_cpu_mem_usage": False},
        )
    return _title_generator


def _generate_cluster_title(complaints, idxs, embeddings):
    """Generates a short (3-6 word) title summarizing the common issue across
    a cluster's complaints. Returns None on any failure so the caller can fall
    back to _representative_subject instead of showing a blank/broken title.

    Samples the most CENTRAL complaints (by embedding similarity), not an
    arbitrary subset -- feeding the model idiosyncratic complaints (e.g. the
    one mentioning a specific block number that doesn't apply to the rest of
    the cluster) makes a small model latch onto that detail and present it as
    if it were the general theme, which is misleading rather than just
    awkwardly phrased."""
    try:
        generator = _get_title_generator()
        ranked = _rank_by_centrality(idxs, embeddings)
        sample_subjects = [complaints[i].subject for i in ranked[:5]]
        prompt = (
            "Summarize the common issue in these resident complaints as a short "
            "title of 3 to 6 words. Do not use full sentences. Describe the general "
            "type of problem only -- do not include specific block numbers, floor "
            "numbers, or apartment numbers even if one complaint mentions one.\n"
            + "\n".join(f"- {s}" for s in sample_subjects)
        )
        output = generator(prompt, max_new_tokens=12, do_sample=False)
        title = output[0]["generated_text"].strip().strip('"').strip(".")
        if not title:
            return None
        return " ".join(word.capitalize() for word in title.split())
    except Exception:  # noqa: BLE001
        return None


def _cluster_category(category, complaints, distance_threshold=DISTANCE_THRESHOLD):
    """Cluster complaints belonging to a single category. Returns a list of
    {category, title, count, complaint_ids} dicts, one per cluster >= MIN_CLUSTER_SIZE."""
    if len(complaints) < MIN_CLUSTER_SIZE:
        return []

    from sklearn.cluster import AgglomerativeClustering

    texts = [f"{c.subject}. {c.description}" for c in complaints]
    embeddings = _embed(texts)

    clusterer = AgglomerativeClustering(
        n_clusters=None,
        distance_threshold=distance_threshold,
        metric="cosine",
        linkage="average",
    )
    labels = clusterer.fit_predict(embeddings)

    results = []
    for label in sorted(set(labels)):
        idxs = [i for i, lbl in enumerate(labels) if lbl == label]
        if len(idxs) < MIN_CLUSTER_SIZE:
            continue

        complaint_ids = [complaints[i].id for i in idxs]
        title = _generate_cluster_title(complaints, idxs, embeddings) or _representative_subject(complaints, idxs, embeddings)

        results.append({
            "category": category,
            "title": title,
            "count": len(idxs),
            "complaint_ids": complaint_ids,
        })

    return results


def _compute_clusters(complaints):
    by_category = defaultdict(list)
    for c in complaints:
        by_category[c.category].append(c)

    all_results = []
    for category, cat_complaints in by_category.items():
        all_results.extend(_cluster_category(category, cat_complaints))

    all_results.sort(key=lambda r: -r["count"])
    return all_results


def get_emerging_issues_for_society(society_id):
    now = time.time()
    cached = _cache.get(society_id)
    if cached and (now - cached["ts"]) < CACHE_TTL_SECONDS:
        return cached["data"]

    complaints = Complaint.query.filter_by(society_id=society_id).all()
    data = _compute_clusters(complaints)
    _cache[society_id] = {"data": data, "ts": now}
    return data


def invalidate_cache(society_id=None):
    """Call this if you want fresher results than the TTL allows
    (e.g. after a batch of new complaints comes in). Safe to ignore otherwise."""
    if society_id is None:
        _cache.clear()
    else:
        _cache.pop(society_id, None)


@emerging_issues_bp.get("")
@roles_required(ROLE_ADMIN)
def list_emerging_issues():
    user = current_user()
    try:
        data = get_emerging_issues_for_society(user.society_id)
    except Exception as exc:  # noqa: BLE001
        current_app.logger.exception("Failed to compute emerging issues")
        return fail(f"Emerging issues computation failed: {exc}", "EMERGING_ISSUES_ERROR", 500)
    return ok(data)


@emerging_issues_bp.get("/debug")
@roles_required(ROLE_ADMIN)
def debug_emerging_issues():
    """DEV-ONLY diagnostic route. For each category, shows:
    - the actual pairwise cosine similarity matrix between complaints (real numbers,
      not a filtered/clustered result) so a distance_threshold can be picked from
      real data instead of guessed
    - what clustering would look like at several candidate thresholds, so you can
      see directly which one groups the right complaints together

    Gated behind app.debug so it never exists in a production/test build. Safe to
    delete entirely (along with its authStore.js/AdminPortalView.vue counterparts)
    once DISTANCE_THRESHOLD above is confirmed working on real data."""
    if not current_app.debug:
        return fail("Not found", "NOT_FOUND", 404)

    user = current_user()
    try:
        complaints = Complaint.query.filter_by(society_id=user.society_id).all()
        by_category = defaultdict(list)
        for c in complaints:
            by_category[c.category].append(c)

        candidate_thresholds = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

        from sklearn.cluster import AgglomerativeClustering
        from sklearn.metrics.pairwise import cosine_similarity

        debug_output = {}
        for category, cat_complaints in by_category.items():
            if len(cat_complaints) < 2:
                debug_output[category] = {
                    "total_complaints": len(cat_complaints),
                    "note": "fewer than 2 complaints, nothing to cluster",
                }
                continue

            texts = [f"{c.subject}. {c.description}" for c in cat_complaints]
            embeddings = _embed(texts)

            sim_matrix = cosine_similarity(embeddings)
            subjects = [c.subject for c in cat_complaints]
            similarity_table = [
                {"subject": subjects[i], **{subjects[j]: round(float(sim_matrix[i][j]), 3) for j in range(len(subjects))}}
                for i in range(len(subjects))
            ]

            threshold_results = {}
            for threshold in candidate_thresholds:
                clusterer = AgglomerativeClustering(
                    n_clusters=None,
                    distance_threshold=threshold,
                    metric="cosine",
                    linkage="average",
                )
                labels = clusterer.fit_predict(embeddings)
                groups = defaultdict(list)
                for subject, label in zip(subjects, labels):
                    groups[int(label)].append(subject)
                threshold_results[str(threshold)] = {
                    "group_sizes": sorted([len(v) for v in groups.values()], reverse=True),
                    "groups": list(groups.values()),
                }

            debug_output[category] = {
                "total_complaints": len(cat_complaints),
                "min_cluster_size_required": MIN_CLUSTER_SIZE,
                "pairwise_cosine_similarity": similarity_table,
                "clustering_at_thresholds": threshold_results,
            }

        return ok(debug_output)
    except Exception as exc:  # noqa: BLE001
        current_app.logger.exception("Emerging issues debug endpoint failed")
        return fail(f"Debug clustering failed: {exc}", "EMERGING_ISSUES_DEBUG_ERROR", 500)
