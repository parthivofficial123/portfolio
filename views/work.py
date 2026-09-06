"""
views/work.py
-------------
Work index page — Phase 1 shell.
Typography and composition only. Real content in Phase 4.
"""

import streamlit as st
from components.navigation import render_navigation
from components.footer import render_footer


def show() -> None:
    render_navigation(current_page="work")

    st.markdown("""
<div class="pp-page">
  <div class="pp-page-header">
    <span class="pp-page-header__folio">Selected Work</span>
    <h1 class="pp-page-header__title">Work</h1>
    <p class="pp-page-header__desc">
      Projects, research, and things built&mdash;or broken&mdash;along the way.
    </p>
  </div>
</div>
""", unsafe_allow_html=True)

    render_footer()


show()
