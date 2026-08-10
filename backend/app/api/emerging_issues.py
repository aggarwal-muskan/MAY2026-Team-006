"""
Emerging Issues API
--------------------
Clusters existing complaints WITHIN each category (Electrical, Maintenance,
Plumbing, Security) using sentence embeddings, labels clusters via a small
local text-generation model, and exposes clusters of size >= MIN_CLUSTER_SIZE
as "emerging issues" cards for the admin dashboard. Each result includes the
list of complaint IDs in that cluster, so the frontend can pull the actual
complaint rows out of whatever list it already has (no separate fetch
needed, and any status/assign change made elsewhere is automatically
reflected here too).

Clustering algorithm: AgglomerativeClustering with cosine distance, not
HDBSCAN. HDBSCAN is density-based and has a "noise" concept (points that
don't get assigned to any cluster) -- that works great on large, messy,
real-world data, but is unreliable on small sample sizes in high-dimensional
embedding spaces (this model produces 384-dim vectors), where density
estimates get unstable. AgglomerativeClustering with a fixed
distance_threshold has no noise concept at all -- every point is assigned to
some cluster -- which sidesteps that whole failure mode. The
>= MIN_CLUSTER_SIZE business rule is then applied afterwards, as a simple
filter on cluster size.

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
# distance of each other. Lower = stricter (only near-duplicates merge).
DISTANCE_THRESHOLD = 0.5

# in-memory cache: {society_id: {"data": [...], "ts": float}}
_cache = {}

_model = None  # lazy-loaded SentenceTransformer, shared across requests
_title_generator = None  # lazy-loaded FLAN-T5 pipeline, shared across requests


def _get_model():
    """Load the sentence-transformer model once and reuse it for every request.
    device="cpu" is passed explicitly as a defensive measure against a known
    PyTorch/transformers compatibility issue where newer transformers versions
    can leave model weights on a placeholder "meta" device."""
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
    (highest average similarity to every other member), most central first."""
    import numpy as np

    cluster_embeddings = embeddings[idxs]
    # embeddings are L2-normalized, so a dot product here is the same as cosine similarity
    similarity_matrix = cluster_embeddings @ cluster_embeddings.T
    total_similarity = similarity_matrix.sum(axis=1)
    order = np.argsort(-total_similarity)  # descending: most central first
    return [idxs[i] for i in order]


def _representative_subject(complaints, idxs, embeddings):
    """Picks the most "central" complaint in a cluster and returns its real
    subject line as the card title. Used as a fallback if title generation
    below is unavailable or fails for any reason."""
    ranked = _rank_by_centrality(idxs, embeddings)
    return complaints[ranked[0]].subject


def _get_title_generator():
    """Loads a small, free, local text-generation model (google/flan-t5-base,
    Apache 2.0 licensed) once and reuses it. Runs entirely offline after the
    first download -- no API key, no per-call cost.

    Uses -base (250M params) rather than -small (80M params): -small was
    tested against real complaint data and consistently just copied one input
    line back verbatim instead of paraphrasing/abstracting, across every
    cluster tried. -base has noticeably better instruction-following at a
    still-modest size that runs fine on CPU.

    Loads the tokenizer + model directly via AutoTokenizer/AutoModelForSeq2SeqLM
    rather than transformers.pipeline("text2text-generation", ...). That pipeline
    task shortcut was removed in transformers v5 (see huggingface/transformers
    issue #44509), so going around it entirely avoids depending on which pipeline
    tasks a given transformers version happens to support.

    device="cpu" and low_cpu_mem_usage=False are both set explicitly to avoid a
    known transformers/accelerate "meta tensor" loading issue that can occur
    when loading a second model in the same process as the sentence-transformer
    above."""
    global _title_generator
    if _title_generator is None:
        from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
        tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
        model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base", low_cpu_mem_usage=False)
        model.to("cpu")
        model.eval()
        _title_generator = (tokenizer, model)
    return _title_generator


def _generate_cluster_title(complaints, idxs, embeddings):
    """Generates a short (3-6 word) title summarizing the common issue across
    a cluster's complaints. Returns None on any failure so the caller can fall
    back to _representative_subject instead of showing a blank/broken title.

    Samples up to 10 complaints from the cluster, ranked by centrality (most
    representative first) -- with your current cluster sizes (6-8), this means
    the model effectively sees the WHOLE cluster, not just a handful of the
    most central ones. Feeding it more of the group's actual variety gives it
    less excuse to just echo a single input line back."""
    try:
        tokenizer, model = _get_title_generator()
        ranked = _rank_by_centrality(idxs, embeddings)
        sample_subjects = [complaints[i].subject for i in ranked[:10]]
        prompt = (
            "Write a short new title, 3 to 6 words, that describes the shared problem "
            "across ALL of these resident complaints -- not just one of them. "
            "Do NOT copy any single complaint's exact wording -- paraphrase in your own "
            "words. Do not overgeneralize: the title should be specific to the actual "
            "problem described (e.g. 'Water Leakage' or 'CCTV Not Working'), not a vague "
            "word like 'Issue' or 'Problem' alone. Do not use full sentences. Do not "
            "include specific block numbers, floor numbers, or apartment numbers even if "
            "one complaint mentions one.\n"
            + "\n".join(f"- {s}" for s in sample_subjects)
        )

        import torch
        inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
        with torch.no_grad():
            output_ids = model.generate(**inputs, max_new_tokens=12, do_sample=False)
        title = tokenizer.decode(output_ids[0], skip_special_tokens=True).strip().strip('"').strip(".")

        if not title:
            return None
        final_title = " ".join(word.capitalize() for word in title.split())
        return final_title
    except Exception as exc:  # noqa: BLE001
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
