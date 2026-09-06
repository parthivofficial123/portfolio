"""
views/about.py
--------------
About page — Phase 1 shell.
Typography and composition only. Real content in Phase 5.
"""

import streamlit as st
from components.navigation import render_navigation
from components.footer import render_footer


def show() -> None:
    render_navigation(current_page="about")

    st.markdown("""
<div class="pp-page">
  <div class="pp-page-header">
    <span class="pp-page-header__folio">About</span>
    <h1 class="pp-page-header__title">About</h1>
    <p class="pp-page-header__desc">
      Engineering, AI, and the questions that connect them.
    </p>
  </div>
</div>
""", unsafe_allow_html=True)

    render_footer()


show()
