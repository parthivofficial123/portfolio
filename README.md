# portfolio

Personal portfolio for Parthiv Patel — built with Streamlit, deployed on Streamlit Community Cloud.

## Status

Pre-development. The design system and content plan are established; the application has not been built yet.

## Repository Structure

```
portfolio/
├── app.py              # Streamlit application entry point (placeholder)
├── requirements.txt    # Python dependencies
├── README.md
└── docs/
    ├── PROJECT_BRIEF.md
    ├── DESIGN_SYSTEM.md
    ├── CONTENT_MAP.md
    └── PRIVACY.md
```

## Documentation (`/docs`)

These documents are the source of truth for all design and development decisions.

| Document | Purpose |
|---|---|
| **PROJECT_BRIEF.md** | Goals, audience, voice & tone, information architecture, conceptual direction, and technical constraints. Start here. |
| **DESIGN_SYSTEM.md** | Visual language: typography, color, spacing, layout principles, component vocabulary, motion guidelines, and a checklist of anti-patterns to avoid. |
| **CONTENT_MAP.md** | Page-by-page inventory of every section, what content it needs, and whether that content is available, needs writing, or needs gathering. |
| **PRIVACY.md** | What personal information may and may not appear on the public site. Non-negotiable — Parthiv is a minor. |

## Running Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```