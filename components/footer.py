"""
components/footer.py
--------------------
Minimal site footer shell. Phase 1: name + year label only.
Contact links and profile links are deferred to Phase 2+.
"""

import streamlit as st


def render_footer() -> None:
    """Render the site footer."""
    html = """
<footer class="pp-footer" role="contentinfo">
  <div class="pp-footer__inner">
    <span class="pp-footer__name">Parthiv Patel</span>
    <span class="pp-footer__meta">PORTFOLIO / 2026</span>
  </div>
</footer>
"""
    st.markdown(html, unsafe_allow_html=True)
