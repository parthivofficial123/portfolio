"""
views/home.py
-------------
Home page — Phase 1 shell.
Typography and composition only. Real content in Phase 2.
"""

import streamlit as st
from components.navigation import render_navigation
from components.footer import render_footer


def show() -> None:
    render_navigation(current_page="home")

    st.markdown("""
<div class="pp-page">
  <div class="pp-hero">
    <span class="pp-hero__meta">Portfolio&thinsp;/&thinsp;2026</span>
    <h1 class="pp-hero__title">Parthiv Patel</h1>
    <p class="pp-hero__subtitle">
      I ask &ldquo;what if?&rdquo; a little too often.
      Sometimes I build the answer.
    </p>
  </div>
</div>
""", unsafe_allow_html=True)

    render_footer()


show()
