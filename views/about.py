"""
views/about.py
--------------
About page — Phase 1 stub.
Typography and layout skeleton only. Real content in Phase 5.
"""

import streamlit as st
from components.navigation import render_navigation
from components.footer import render_footer


def show() -> None:
    render_navigation(current_path="/about")

    st.markdown("""
<div class="pp-page">
  <div class="pp-hero">
    <span class="pp-hero__meta">About</span>
    <h1 class="pp-hero__title">About</h1>
    <p class="pp-hero__subtitle">
      Engineering, AI, and the questions that connect them.
    </p>
  </div>
</div>
""", unsafe_allow_html=True)

    render_footer()
