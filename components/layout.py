"""
components/layout.py
--------------------
Injects global CSS and provides the page wrapper used by every view.
"""

import streamlit as st
from pathlib import Path


def _load_css() -> str:
    css_path = Path(__file__).parent.parent / "assets" / "css" / "style.css"
    return css_path.read_text(encoding="utf-8")


def inject_global_css() -> None:
    """Call once in app.py before st.navigation. Loads the stylesheet."""
    css = _load_css()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
