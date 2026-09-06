"""
views/work.py
-------------
Work index page — Phase 1 stub.
Typography and layout skeleton only. Real content in Phase 4.
"""

import streamlit as st
from components.navigation import render_navigation
from components.footer import render_footer


def show() -> None:
    render_navigation(current_path="/work")

    st.markdown("""
<div class="pp-page">
  <div class="pp-hero">
    <span class="pp-hero__meta">Work</span>
    <h1 class="pp-hero__title">Work</h1>
    <p class="pp-hero__subtitle">
      Projects, research, and things built — or broken — along the way.
    </p>
  </div>
</div>
""", unsafe_allow_html=True)

    render_footer()


show()
