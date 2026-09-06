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
# url_path must match the hrefs used in components/navigation.py.
# default=True marks the page rendered at the root URL ("/").
# ---------------------------------------------------------------------------

home_page  = st.Page("views/home.py",  title="Home",  url_path="home",  default=True)
work_page  = st.Page("views/work.py",  title="Work",  url_path="work")
about_page = st.Page("views/about.py", title="About", url_path="about")

pg = st.navigation(
    [home_page, work_page, about_page],
    position="hidden",   # hides Streamlit's built-in sidebar nav
)

pg.run()
