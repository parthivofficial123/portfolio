"""
components/navigation.py
------------------------
Renders the custom top navigation bar.

st.navigation / st.Page handles routing. This component renders the
visible nav HTML. Active state is determined by comparing the current
page's URL path against each link.
"""

import streamlit as st


# Map display label → URL path (must match the url_path= set in st.Page)
NAV_ITEMS = [
    ("HOME",  "/home"),
    ("WORK",  "/work"),
    ("ABOUT", "/about"),
]


def render_navigation(current_path: str = "/") -> None:
    """
    Render the sticky top navigation bar.

    Args:
        current_path: The URL path of the current page, e.g. "/" or "/work".
    """
    links_html = ""
    for label, path in NAV_ITEMS:
        active_class = " pp-nav__link--active" if current_path == path else ""
        links_html += (
            f'<li>'
            f'<a href="{path}" class="pp-nav__link{active_class}" '
            f'aria-current="{"page" if current_path == path else "false"}">'
            f'{label}'
            f'</a>'
            f'</li>'
        )

    html = f"""
<nav class="pp-nav" role="navigation" aria-label="Primary navigation">
  <div class="pp-nav__inner">
    <a href="/" class="pp-nav__brand">Parthiv Patel</a>
    <ul class="pp-nav__links">
      {links_html}
    </ul>
  </div>
</nav>
"""
    st.markdown(html, unsafe_allow_html=True)
