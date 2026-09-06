"""
components/navigation.py
------------------------
Renders the custom top navigation bar using st.page_link() for all
routing links. st.page_link() is Streamlit-aware — it generates correct
href values and never produces a 404, unlike raw <a href> tags which
bypass Streamlit's SPA router.

Layout:
  LEFT  — brand "Parthiv Patel"  (st.page_link, styled as brand)
  RIGHT — HOME  WORK  ABOUT      (st.page_link, styled as nav items)

Active state is indicated by a sienna underline rule beneath the current
page label.

CSS handles all visual styling. The st.page_link elements are wrapped in
a container div so we can target them precisely without affecting other
Streamlit link components.
"""

import streamlit as st

# (label, page_file, url_path) — url_path used only for active-state check
NAV_ITEMS = [
    ("HOME",  "views/home.py",  "home"),
    ("WORK",  "views/work.py",  "work"),
    ("ABOUT", "views/about.py", "about"),
]


def render_navigation(current_page: str = "home") -> None:
    """
    Render the sticky top navigation bar.

    Args:
        current_page: url_path of the current page, e.g. "home", "work", "about".
    """
    # Thin rule separator injected via markdown so it sits flush
    # The nav wrapper div is used by CSS for sticky positioning + border-bottom
    st.markdown('<div class="pp-nav-wrap">', unsafe_allow_html=True)

    # Single row: brand left, nav links right
    col_brand, col_spacer, col_home, col_work, col_about = st.columns(
        [3, 4, 1, 1, 1], gap="small"
    )

    with col_brand:
        st.markdown('<div class="pp-nav-brand-wrap">', unsafe_allow_html=True)
        st.page_link("views/home.py", label="Parthiv Patel")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_home:
        active = current_page == "home"
        st.markdown(
            f'<div class="pp-nav-item{"  pp-nav-item--active" if active else ""}">',
            unsafe_allow_html=True,
        )
        st.page_link("views/home.py", label="HOME")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_work:
        active = current_page == "work"
        st.markdown(
            f'<div class="pp-nav-item{"  pp-nav-item--active" if active else ""}">',
            unsafe_allow_html=True,
        )
        st.page_link("views/work.py", label="WORK")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_about:
        active = current_page == "about"
        st.markdown(
            f'<div class="pp-nav-item{"  pp-nav-item--active" if active else ""}">',
            unsafe_allow_html=True,
        )
        st.page_link("views/about.py", label="ABOUT")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)  # close pp-nav-wrap

    # Thin rule beneath nav
    st.markdown('<hr class="pp-nav-rule" />', unsafe_allow_html=True)
