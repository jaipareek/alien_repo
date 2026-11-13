"""
app.py — Main entry point for OMNITRIX LAB.
Sets page config, loads custom CSS, renders sidebar navigation,
and routes to the selected page.
"""

import streamlit as st
import os

# --- Page Configuration (must be the very first Streamlit call) ---
st.set_page_config(
    page_title="OMNITRIX LAB ⚡",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Load Custom CSS ---
css_path = os.path.join(os.path.dirname(__file__), "assets", "style.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Import Page Modules ---
from pages_code import omnitrix, vault, analytics, data_lab, gallery, arena
from utils.helpers import render_header

# --- Navigation Pages List ---
PAGES = [
    "⌚ Omnitrix",
    "🗃️ Alien Vault",
    "📊 Analytics",
    "🧪 Data Lab",
    "🖼️ Gallery",
    "⚔️ Battle Arena",
]

# --- Sidebar Navigation ---
with st.sidebar:
    # Logo / Title
    st.markdown(
        """
        <div style="text-align:center; padding: 1rem 0 0.5rem 0;">
            <div style="font-size: 2.5rem;">⚡</div>
            <div style="font-family: 'Orbitron', sans-serif; color: #39ff14;
                        font-size: 1.2rem; letter-spacing: 4px;
                        text-shadow: 0 0 10px #39ff1488;">
                OMNITRIX LAB
            </div>
            <div style="color: #888; font-size: 0.75rem; letter-spacing: 2px;
                        font-family: 'Rajdhani', sans-serif; margin-top: 2px;">
                Superhero Analytics
            </div>
        </div>
        <hr style="border-color: #1a8a0a; margin: 0.5rem 0 1rem 0;">
        """,
        unsafe_allow_html=True,
    )

    page = st.radio(
        "NAVIGATE",
        PAGES,
        key="main_nav_page",
    )

    # Footer
    st.markdown(
        """
        <div style="margin-top: 3rem; color: #555; font-size: 0.75rem;
                    font-family: 'Rajdhani', sans-serif; letter-spacing: 1px; text-align: center;">
            OMNITRIX SYSTEM v2.0<br>
            <span style="color:#39ff14;">Galvan Prime Certified</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

# --- Render Header ---
render_header()

# --- Page Content (with fade-in wrapper) ---
st.markdown('<div class="fade-in">', unsafe_allow_html=True)

if page == "⌚ Omnitrix":
    omnitrix.show()
elif page == "🗃️ Alien Vault":
    vault.show()
elif page == "📊 Analytics":
    analytics.show()
elif page == "🧪 Data Lab":
    data_lab.show()
elif page == "🖼️ Gallery":
    gallery.show()
elif page == "⚔️ Battle Arena":
    arena.show()

st.markdown("</div>", unsafe_allow_html=True)
