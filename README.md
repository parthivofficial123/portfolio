# portfolio

Personal portfolio for Parthiv Patel — built with Streamlit, deployed on Streamlit Community Cloud.

## Status

**Phase 1 complete.** The application shell is implemented: routing, global CSS, typography, color tokens, navigation, footer, and responsive layout are in place. Content phases begin next.

## Repository Structure

```
portfolio/
├── app.py                  # Entry point — routing via st.navigation + st.Page
├── requirements.txt        # Python dependencies
├── README.md
├── .streamlit/
│   └── config.toml         # Theme config (eliminates load flash, Cloud deployment)
├── assets/
│   ├── css/
│   │   └── style.css       # Single centralized stylesheet
│   └── (images added from Phase 3 onward)
├── components/
│   ├── layout.py           # CSS injection
│   ├── navigation.py       # Top nav bar (st.page_link)
│   └── footer.py           # Footer shell
├── content/
│   └── __init__.py         # Content package — populated from Phase 2
├── views/
│   ├── home.py             # Home page
│   ├── work.py             # Work index
│   └── about.py            # About page
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
| **PROJECT_BRIEF.md** | Goals, audience, voice & tone, information architecture, conceptual direction, technical constraints, and implementation phases. Start here. |
| **DESIGN_SYSTEM.md** | Visual language: typography, color, spacing, layout principles, component vocabulary, motion guidelines, and an anti-patterns checklist. |
| **CONTENT_MAP.md** | Page-by-page inventory of every section, what content it needs, and current availability. |
| **PRIVACY.md** | What personal information may and may not appear on the public site. Non-negotiable — Parthiv is a minor. |

## Running Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```
