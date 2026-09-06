"""
views/work/serc.py
------------------
USC SERC project detail page — Phase 3.

Privacy: no other researchers named, no unpublished methods described,
media placeholders note disclosure review is required.
"""

import streamlit as st
from components.navigation import render_navigation
from components.footer import render_footer
from content.serc import meta, sections


def _media_placeholder(label: str) -> None:
    """Render a media placeholder block."""
    st.markdown(
        f'<div class="pp-media-placeholder pp-media-placeholder--4-3">'
        f'<span class="pp-media-placeholder__label">{label}</span>'
        f'</div>',
        unsafe_allow_html=True,
    )


def show() -> None:
    render_navigation(current_page="work")

    # Back link
    st.markdown('<div class="pp-detail-header__back">', unsafe_allow_html=True)
    st.page_link("views/work.py", label="← Work")
    st.markdown("</div>", unsafe_allow_html=True)

    # Page header
    st.markdown(
        f"""
<div class="pp-detail-header">
  <span class="pp-detail-header__folio">{meta["folio"]}</span>
  <h1 class="pp-detail-header__title">{meta["title"]}</h1>
  <span class="pp-detail-header__meta">{meta["meta_line"]}</span>
  <span class="pp-detail-header__tech">{meta["tech"]}</span>
</div>
""",
        unsafe_allow_html=True,
    )

    # Opening section (no label)
    opening = sections[0]
    st.markdown('<div class="pp-detail-section">', unsafe_allow_html=True)
    st.markdown('<div class="pp-detail-section__body">', unsafe_allow_html=True)
    for para in opening["content"]:
        st.markdown(f"<p>{para}</p>", unsafe_allow_html=True)
    st.markdown("</div></div>", unsafe_allow_html=True)

    # Remaining sections
    for section in sections[1:]:
        st.markdown('<div class="pp-detail-section">', unsafe_allow_html=True)

        if "label" in section:
            st.markdown(
                f'<span class="pp-detail-section__label">{section["label"]}</span>',
                unsafe_allow_html=True,
            )

        if section.get("type") == "prose":
            st.markdown('<div class="pp-detail-section__body">', unsafe_allow_html=True)
            for para in section.get("content", []):
                st.markdown(f"<p>{para}</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

        if "media" in section:
            _media_placeholder(section["media"])

        st.markdown("</div>", unsafe_allow_html=True)

    # Bottom back link
    st.markdown('<div class="pp-detail-back">', unsafe_allow_html=True)
    st.page_link("views/work.py", label="← Work")
    st.markdown("</div>", unsafe_allow_html=True)

    render_footer()


show()
