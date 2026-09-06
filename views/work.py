"""
views/work.py
-------------
Work index page — Phase 3.
Typographic list of flagship entries + supporting work.
No card grid.
"""

import streamlit as st
from components.navigation import render_navigation
from components.footer import render_footer


def show() -> None:
    render_navigation(current_page="work")

    # ── Page header ──────────────────────────────────────────────────────────
    st.markdown("""
<div class="pp-page">
  <div class="pp-page-header">
    <span class="pp-page-header__folio">Work</span>
    <h1 class="pp-page-header__title">Work</h1>
    <p class="pp-page-header__desc">Projects, research, and the work behind them.</p>
  </div>
</div>
""", unsafe_allow_html=True)

    # ── Flagship entry 01 — JARVIS ───────────────────────────────────────────
    st.markdown('<div class="pp-work-entry">', unsafe_allow_html=True)
    st.markdown('<span class="pp-work-entry__number">01</span>', unsafe_allow_html=True)
    st.markdown('<div class="pp-work-entry__title-link">', unsafe_allow_html=True)
    st.page_link("views/work/jarvis.py", label="JARVIS")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown(
        '<span class="pp-work-entry__status">On hold</span>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="pp-work-entry__desc">A personal AI assistant built from scratch over two years'
        " \u2014 speech, vision, local LLM, and a lot of rebuilding.</p>",
        unsafe_allow_html=True,
    )
    st.markdown(
        '<span class="pp-work-entry__tech">Faster-Whisper / Llama\u00a03 / Ollama / OpenCV / YOLOv8</span>',
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)  # close pp-work-entry

    st.markdown('<hr class="pp-rule" />', unsafe_allow_html=True)

    # ── Flagship entry 02 — USC SERC ─────────────────────────────────────────
    st.markdown('<div class="pp-work-entry">', unsafe_allow_html=True)
    st.markdown('<span class="pp-work-entry__number">02</span>', unsafe_allow_html=True)
    st.markdown('<div class="pp-work-entry__title-link">', unsafe_allow_html=True)
    st.page_link("views/work/serc.py", label="USC SERC / ISI")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown(
        '<span class="pp-work-entry__status">Completed</span>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="pp-work-entry__desc">Six weeks at a USC engineering lab, ending with a'
        " self-directed digital-twin simulation of a spacecraft.</p>",
        unsafe_allow_html=True,
    )
    st.markdown(
        '<span class="pp-work-entry__tech">ROS\u00a02 Jazzy / Gazebo Ignition / Siemens NX / CAD</span>',
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<hr class="pp-rule" />', unsafe_allow_html=True)

    # ── Flagship entry 03 — FRC ───────────────────────────────────────────────
    st.markdown('<div class="pp-work-entry">', unsafe_allow_html=True)
    st.markdown('<span class="pp-work-entry__number">03</span>', unsafe_allow_html=True)
    st.markdown('<div class="pp-work-entry__title-link">', unsafe_allow_html=True)
    st.page_link("views/work/frc.py", label="FRC")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown(
        '<span class="pp-work-entry__status">Ongoing</span>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p class="pp-work-entry__desc">CAD, fabrication, and the physical side of engineering,'
        " building competition robots through to the FIRST World Championship.</p>",
        unsafe_allow_html=True,
    )
    st.markdown(
        '<span class="pp-work-entry__tech">CAD / CNC / Fabrication / Mechanical Assembly</span>',
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # ── Separator + supporting work ───────────────────────────────────────────
    st.markdown("""
<hr class="pp-rule" />
<span class="pp-section-label">Supporting work</span>
""", unsafe_allow_html=True)

    # CS Club
    st.markdown("""
<div class="pp-work-supporting">
  <span class="pp-work-supporting__title">CS Club</span>
  <div class="pp-work-supporting__body">
    <p>Helped found the school&#8217;s CS club as a member of the founding board.
    Organized two hackathons and introductory programming sessions for students
    who hadn&#8217;t touched code before. More clubs followed.</p>
  </div>
</div>
""", unsafe_allow_html=True)

    # "More as it happens." line
    st.markdown('<p class="pp-work-more">More as it happens.</p>', unsafe_allow_html=True)

    render_footer()


show()
