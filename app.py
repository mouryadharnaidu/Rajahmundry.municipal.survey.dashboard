import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Rajahmundry Municipal Election Opinion Survey",
    layout="wide",
    initial_sidebar_state="collapsed"
)

html_path = Path(__file__).parent / "Rajahmundry_Dashboard.html"

if not html_path.exists():
    st.error("Rajahmundry_Dashboard.html was not found. Keep it in the same folder as app.py.")
else:
    html_content = html_path.read_text(encoding="utf-8")
    components.html(
        html_content,
        height=1100,
        scrolling=True
    )
