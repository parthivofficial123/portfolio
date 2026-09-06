"""
app.py
------
Application entry point.
Configures the Streamlit app, injects global CSS, and defines routing
using st.navigation + st.Page (Streamlit >= 1.36).

The sidebar is hidden via CSS. The custom navigation bar in each view
provides all top-level routing.
"""

import streamlit as st
from components.layout import inject_global_css

st.set_page_config(
    page_title="Parthiv Patel",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items=None,
)

inject_global_css()

# ---------------------------------------------------------------------------
# Routing
# ---------------------------------------------------------------------------
# st.Page registers each view at its url_path.
# st.navigation with position="hidden" suppresses Streamlit's built-in
# sidebar nav — our custom nav bar in components/navigation.py takes over.
# default=True on home_page means "/" renders the Home view.
# ---------------------------------------------------------------------------

home_page  = st.Page("views/home.py",  title="Home",  url_path="home",  default=True)
work_page  = st.Page("views/work.py",  title="Work",  url_path="work")
about_page = st.Page("views/about.py", title="About", url_path="about")

# Phase 3 — work detail pages
jarvis_page = st.Page("views/work/jarvis.py", title="JARVIS",         url_path="work/jarvis")
serc_page   = st.Page("views/work/serc.py",   title="USC SERC / ISI", url_path="work/serc")
frc_page    = st.Page("views/work/frc.py",    title="FRC",            url_path="work/frc")

pg = st.navigation(
    [home_page, work_page, about_page, jarvis_page, serc_page, frc_page],
    position="hidden",   # hides Streamlit's built-in sidebar nav
)

pg.run()
