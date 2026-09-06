"""
components/navigation.py
------------------------
Renders the top navigation bar using st.page_link() for all routing links.

st.page_link() is Streamlit-aware — it generates correct SPA-compatible
hrefs that never produce a 404, unlike raw <a href> tags.

Layout:
  LEFT  — brand "Parthiv Patel"   → links to Home
  RIGHT — HOME  WORK  ABOUT       → page links

Active state: a sienna underline is applied beneath the current page label
via the .pp-nav-item--active CSS class.

All visual styling is in assets/css/style.css.
"""

import streamlit as st


def render_navigation(current_page: str = "home") -> None:
    """
    Render the sticky top navigation bar.

    Args:
        current_page: url_path slug of the current page ("home", "work", "about").
    """
    st.markdown('<div class="pp-nav-wrap">', unsafe_allow_html=True)

    # Columns: brand (left, wide) | spacer | HOME | WORK | ABOUT
    col_brand, col_home, col_work, col_about = st.columns(
        [5, 1, 1, 1], gap="small"
    )

    with col_brand:
        st.markdown('<div class="pp-nav-brand-wrap">', unsafe_allow_html=True)
        st.page_link("views/home.py", label="Parthiv Patel")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_home:
        active = "pp-nav-item--active" if current_page == "home" else ""
        st.markdown(f'<div class="pp-nav-item {active}">', unsafe_allow_html=True)
        st.page_link("views/home.py", label="HOME")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_work:
        active = "pp-nav-item--active" if current_page == "work" else ""
        st.markdown(f'<div class="pp-nav-item {active}">', unsafe_allow_html=True)
        st.page_link("views/work.py", label="WORK")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_about:
        active = "pp-nav-item--active" if current_page == "about" else ""
        st.markdown(f'<div class="pp-nav-item {active}">', unsafe_allow_html=True)
        st.page_link("views/about.py", label="ABOUT")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)  # close .pp-nav-wrap

    # Thin rule beneath nav
    st.markdown('<hr class="pp-nav-rule" />', unsafe_allow_html=True)
