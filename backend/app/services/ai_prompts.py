SOCIETY_SYSTEM = (
    "You are an AI assistant for SocioNeed, an Indian residential housing society "
    "management app. Be clear, formal, practical, and resident-friendly. "
    "Do not invent fees, resident names, or fake facts. Do not give legal or medical advice."
)


def notice_generator_prompt(topic: str, date: str, time_range: str, extra: str) -> str:
    return f"""
Write a professional society notice from these details.

Topic: {topic or 'Society update'}
Date: {date or 'To be announced'}
Time: {time_range or 'To be announced'}
Additional information: {extra or 'None'}

Return JSON only with this shape:
{{
  "title": "short notice title",
  "body": "full notice body with Dear Residents greeting and closing"
}}
""".strip()


def translate_announcement_prompt(text: str, languages: list[str]) -> str:
    langs = ", ".join(languages)
    return f"""
Translate the following society announcement into these languages: {langs}.
Keep meaning accurate and suitable for residential society communication.

Announcement:
{text}

Return JSON only:
{{
  "translations": {{
    "English": "...",
    "Hindi": "...",
    "Telugu": "..."
  }}
}}
Include only the requested languages as keys.
""".strip()


def event_planner_prompt(
    event_name: str,
    expected_residents: int | None,
    duration: str,
    budget: str,
    notes: str,
) -> str:
    return f"""
Create a practical event plan for an Indian residential society.

Event: {event_name}
Expected residents: {expected_residents if expected_residents is not None else 'not specified'}
Duration: {duration or 'not specified'}
Budget: {budget or 'not specified'}
Extra notes: {notes or 'None'}

Return JSON only:
{{
  "title": "event plan title",
  "schedule": ["step 1", "step 2"],
  "resources": ["item"],
  "volunteers": ["role"],
  "checklist": ["task"],
  "announcement_draft": "short invitation text",
  "plan_markdown": "readable multi-section plan"
}}
""".strip()


def analytics_insights_prompt(stats: dict) -> str:
    return f"""
Interpret these aggregated society statistics for an administrator.
Do not invent numbers. Use only the provided values.

Stats JSON:
{stats}

Return JSON only:
{{
  "insight": "2-4 sentence plain-language insight",
  "suggested_actions": ["action 1", "action 2"],
  "highlights": ["short highlight"]
}}
""".strip()


def complaint_classify_prompt(subject: str, description: str) -> str:
    return f"""
Classify this society complaint.

Subject: {subject}
Description: {description}

Choose category from:
Water, Electricity, Security, Parking, Cleaning, Lift, Maintenance, Garden, Noise, Plumbing, Other

Choose priority from: High, Medium, Low
Choose sentiment from: Negative, Neutral, Positive

Return JSON only:
{{
  "category": "Water",
  "priority": "High",
  "sentiment": "Negative",
  "confidence": 0.0,
  "rationale": "one short sentence"
}}
""".strip()


def meeting_minutes_prompt(notes: str, meeting_title: str, meeting_date: str) -> str:
    return f"""
Convert these society committee meeting notes into formal minutes.

Meeting title: {meeting_title or 'Society Committee Meeting'}
Meeting date: {meeting_date or 'Not specified'}
Notes:
{notes}

Return JSON only:
{{
  "title": "meeting minutes title",
  "key_discussions": ["..."],
  "decisions": ["..."],
  "action_items": [
    {{"task": "...", "responsible": "...", "deadline": "..."}}
  ],
  "minutes_markdown": "full readable minutes"
}}
""".strip()


def notice_summarizer_prompt(title: str, body: str) -> str:
    return f"""
Summarize this society notice for busy residents.

Title: {title}
Body:
{body}

Return JSON only:
{{
  "what": "...",
  "when": "...",
  "where": "...",
  "impact": "...",
  "action": "...",
  "summary": "short combined summary"
}}
""".strip()


def notices_summarize_all_prompt(notices: list[dict]) -> str:
    return f"""
Summarize ALL of these active society notices into ONE combined digest for
busy residents. Group related items by theme (Maintenance, Events, Payments,
Security, Other). Each line should be short and answer What / When / Impact / Action.
Use only the provided notices. Do not invent notices or dates.

Notices JSON:
{notices}

Return JSON only:
{{
  "headline": "one-line 'this week in your society' style headline",
  "groups": [
    {{"theme": "Maintenance", "items": ["short line", "short line"]}}
  ],
  "digest_markdown": "full readable combined summary grouped by theme"
}}
""".strip()


def complaint_resolution_insights_prompt(stats: dict) -> str:
    return f"""
Interpret these AGGREGATED complaint-resolution statistics for a society admin.
Focus on backlog, slow categories, and recurring issues. Recommend root-cause
actions, not per-ticket replies. Do not invent numbers or resident names.

Stats JSON:
{stats}

Return JSON only:
{{
  "insight": "2-4 sentence plain-language finding about backlog and patterns",
  "recurring_issues": ["short description of a recurring pattern"],
  "recommended_actions": ["action 1", "action 2"],
  "highlights": ["short highlight"]
}}
""".strip()


def rules_qa_prompt(question: str, documents: str) -> str:
    return f"""
Answer the resident's question STRICTLY from the society documents below
(notices, bylaws, rules). Do not use outside knowledge. Do not invent rules
or fees. If the answer is not present in the documents, set "answered" to false
and say it is not covered.

Society documents:
{documents}

Resident question:
{question}

Return JSON only:
{{
  "answered": true,
  "answer": "concise answer grounded in the documents",
  "source_hint": "which notice/section the answer came from, if any"
}}
""".strip()


def feedback_analyze_prompt(goal: str, poll_question: str, responses: list[str]) -> str:
    return f"""
You help a society committee with polls and resident feedback.
If poll_question is empty, DRAFT a clear poll/survey from the goal.
If responses are provided, summarize them into main themes, sentiment split,
and a suggested next step. Summarize themes and counts only; never attribute
quotes to named residents. Do not invent numbers beyond the given responses.

Goal: {goal or 'not specified'}
Poll question: {poll_question or 'none - draft one'}
Responses JSON:
{responses}

Return JSON only:
{{
  "draft_poll": {{"question": "...", "options": ["..."]}},
  "themes": [{{"theme": "...", "mentions": 0}}],
  "sentiment": {{"positive": 0, "neutral": 0, "negative": 0}},
  "suggested_next_step": "...",
  "summary_markdown": "readable summary"
}}
Return draft_poll only when drafting; otherwise it may be null.
""".strip()


def amenity_booking_prompt(request_text: str, existing_bookings: list[dict]) -> str:
    return f"""
Help a resident book a shared society amenity (clubhouse, gym, party hall,
courts) in plain language. Using the existing bookings provided, suggest free
slots and flag any conflicts or capacity concerns. You only PROPOSE slots; the
app confirms and writes the booking. Do not invent existing bookings.

Resident request:
{request_text}

Existing bookings JSON:
{existing_bookings}

Return JSON only:
{{
  "amenity": "detected amenity or 'unspecified'",
  "requested_when": "detected date/time or 'unspecified'",
  "conflicts": ["short conflict note"],
  "suggested_slots": ["human-readable slot suggestion"],
  "note": "short guidance for the resident",
  "confirmation_required": true
}}
""".strip()


def maintenance_assistant_prompt(query: str, equipment: str, notes: str) -> str:
    return f"""
Help with residential society preventive maintenance.

Equipment: {equipment or 'General'}
Admin notes: {notes or 'None'}
Question / request: {query}

Return JSON only:
{{
  "equipment": "...",
  "maintenance_type": "...",
  "checklist": ["item"],
  "recommended_follow_up": "...",
  "assistant_markdown": "readable guidance"
}}
""".strip()
