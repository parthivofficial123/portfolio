"""
views/home.py
-------------
Home page — Phase 2.

Sections:
  1. Hero
  2. Selected Work (three flagship projects, each with a distinct layout)
  3. Right Now
  4. Away from the Computer / About preview

Content data lives in content/home.py and content/projects.py.
Routing uses st.page_link() — no raw <a href> tags for navigation.

Project detail CTAs:
  Detail pages don't exist yet (Phase 4).
  Each CTA renders as a styled non-interactive placeholder.
  When a detail page is added, set detail_page in content/projects.py
  and the CTA will automatically become a live st.page_link.
"""

import streamlit as st
from components.navigation import render_navigation
from components.footer import render_footer
from content.home import hero, right_now, away
from content.projects import projects


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _media_placeholder(label: str, ratio: str = "4-3") -> None:
    """Render a clearly-labeled media placeholder block."""
    st.markdown(
        f'<div class="pp-media-placeholder pp-media-placeholder--{ratio}" '
        f'role="img" aria-label="Media placeholder: {label.replace(chr(10), " ")}">'
        f'<span class="pp-media-placeholder__label">{label}</span>'
        f'</div>',
        unsafe_allow_html=True,
    )


def _project_cta(project: dict) -> None:
    """
    Render the project CTA.
    If detail_page is set, use st.page_link (live route).
    If not, render a styled placeholder span (no broken route).
    """
    if project["detail_page"]:
        # Live when Phase 4 detail page exists
        st.markdown('<div class="pp-project__cta">', unsafe_allow_html=True)
        st.page_link(project["detail_page"], label=project["cta_label"])
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        # Pending — clearly styled but non-navigating
        # Renders as a span so keyboard users are not misled by a fake link
        st.markdown(
            f'<span class="pp-project__cta pp-project__cta--pending" '
            f'title="Detail page coming in Phase 4">'
            f'{project["cta_label"]}'
            f'</span>',
            unsafe_allow_html=True,
        )


def _project_text_block(project: dict) -> None:
    """Render index, title, meta, body paragraphs, tech, and CTA."""
    slug = project["slug"]
    paragraphs = "".join(
        f"<p>{p}</p>" for p in project["body"]
    )
    st.markdown(
        f"""
<div class="pp-project {f'pp-project--{slug}'}">
  <span class="pp-project__index">{project["index"]}</span>
  <h2 class="pp-project__title">{project["title"]}</h2>
  <span class="pp-project__meta">{project["meta"]}</span>
  <div class="pp-project__body">{paragraphs}</div>
  <span class="pp-project__tech">{project["tech"]}</span>
</div>
""",
        unsafe_allow_html=True,
    )
    _project_cta(project)


# ---------------------------------------------------------------------------
# Section renderers
# ---------------------------------------------------------------------------

def _render_hero() -> None:
    body_paras = "".join(f"<p>{p}</p>" for p in hero["body"])
    st.markdown(
        f"""
<div class="pp-page">
  <div class="pp-hero">
    <h1 class="pp-hero__title">{hero["name"]}</h1>
    <div class="pp-hero__subtitle">{body_paras}</div>
    <span class="pp-hero__cue">{hero["scroll_cue"]}</span>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )


def _render_selected_work() -> None:
    jarvis = projects[0]   # 01 / JARVIS
    serc   = projects[1]   # 02 / USC SERC
    frc    = projects[2]   # 03 / FIRST Robotics

    st.markdown(
        """
<div class="pp-page">
  <hr class="pp-rule" />
  <span class="pp-section-label">Selected Work</span>
</div>
""",
        unsafe_allow_html=True,
    )

    # ── 01 / JARVIS ─────────────────────────────────────────────────────────
    # Layout: large text left (60%) | media placeholder right (40%)
    # Strongest feature — largest title, most copy
    st.markdown('<div class="pp-page">', unsafe_allow_html=True)
    col_text, col_media = st.columns([6, 4], gap="large")
    with col_text:
        _project_text_block(jarvis)
    with col_media:
        _media_placeholder(jarvis["media_label"], ratio="4-3")
    st.markdown("</div>", unsafe_allow_html=True)

    # ── 02 / USC SERC ────────────────────────────────────────────────────────
    # Layout: media placeholder left (45%) | text right (55%) — reversed
    # More structured, tighter text block
    st.markdown('<div class="pp-page">', unsafe_allow_html=True)
    col_media, col_text = st.columns([4, 5], gap="large")
    with col_media:
        _media_placeholder(serc["media_label"], ratio="4-3")
    with col_text:
        _project_text_block(serc)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── 03 / FIRST Robotics ──────────────────────────────────────────────────
    # Layout: wide media placeholder full-width at top, short text below
    # Visual / manufacturing emphasis — widest media treatment
    st.markdown('<div class="pp-page">', unsafe_allow_html=True)
    _media_placeholder(frc["media_label"], ratio="16-9")
    # Text below, constrained to left half so it doesn't stretch awkwardly
    col_text, col_empty = st.columns([5, 3], gap="large")
    with col_text:
        _project_text_block(frc)
    st.markdown("</div>", unsafe_allow_html=True)


def _render_right_now() -> None:
    st.markdown(
        """
<div class="pp-page">
  <hr class="pp-rule" />
  <span class="pp-section-label">Right Now</span>
  <p style="font-family:var(--font-sans);font-size:var(--text-sm);
             color:var(--color-text-secondary);margin:0 0 var(--sp-5) 0;
             max-width:52ch;">
    Not everything I&#8217;m doing deserves its own project page.
  </p>
</div>
""",
        unsafe_allow_html=True,
    )

    # Build the index list as one HTML block
    items_html = ""
    for category, text in right_now:
        # "December." entry — split on newline for highlight + subtext treatment
        if "\n" in text:
            lines = text.split("\n", 1)
            text_html = (
                f'<span class="pp-now__text pp-now__text--highlight">{lines[0]}</span>'
                f'<span class="pp-now__subtext">{lines[1]}</span>'
            )
        else:
            text_html = f'<span class="pp-now__text">{text}</span>'

        items_html += (
            f'<li class="pp-now__item">'
            f'<span class="pp-now__category">{category}</span>'
            f'<div>{text_html}</div>'
            f'</li>'
        )

    st.markdown(
        f'<div class="pp-page"><div class="pp-now">'
        f'<ul class="pp-now__list" role="list">{items_html}</ul>'
        f'</div></div>',
        unsafe_allow_html=True,
    )


def _render_about_preview() -> None:
    body_paras = "".join(f"<p>{p}</p>" for p in away["body"])
    st.markdown(
        f"""
<div class="pp-page">
  <div class="pp-about-preview">
    <span class="pp-section-label">Away from the computer</span>
    <div class="pp-about-preview__body">{body_paras}</div>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )
    # About CTA — links to the real About page via st.page_link
    st.markdown('<div class="pp-page"><div class="pp-about-preview__cta-wrap">',
                unsafe_allow_html=True)
    st.page_link("views/about.py", label=away["cta_label"])
    st.markdown("</div></div>", unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Page entry point
# ---------------------------------------------------------------------------

def show() -> None:
    render_navigation(current_page="home")
    _render_hero()
    _render_selected_work()
    _render_right_now()
    _render_about_preview()
    render_footer()


show()
