"""
helpers.py — Shared utility functions for Omnitrix Lab.
Loads CSV data and provides reusable helper functions.
"""

import streamlit as st
import pandas as pd
import os


@st.cache_data
def load_alien_data():
    """Load the aliens.csv file and return a DataFrame.
    Uses st.cache_data so the file is only read once."""
    csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "aliens.csv")
    df = pd.read_csv(csv_path)
    return df


def render_header():
    """Render the animated gradient header at the top of every page."""
    st.markdown(
        """
        <div class="main-header">
            <h1>⚡ OMNITRIX LAB ⚡</h1>
            <p>Superhero Analytics Dashboard</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_section_title(title):
    """Render a styled section title."""
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)


def render_kpi_card(label, value):
    """Render a single KPI metric card."""
    return f'<div class="kpi-card"><div class="kpi-value">{value}</div><div class="kpi-label">{label}</div></div>'


from utils.alien_graphics import get_alien_svg


def render_alien_card_html(alien):
    """Generate the HTML for a single alien card (used in Vault and Omnitrix pages)."""
    # Build stat bars for strength, speed, defense, intelligence
    stats = {
        "STR": alien["strength"],
        "SPD": alien["speed"],
        "DEF": alien["defense"],
        "INT": alien["intelligence"],
    }
    stat_bars = "".join([
        f'<div class="stat-label"><span>{name}</span><span>{val}</span></div>'
        f'<div class="stat-bar-container"><div class="stat-bar" style="width: {val}%;"></div></div>'
        for name, val in stats.items()
    ])
    alien_art = get_alien_svg(alien["name"])
    card_html = (
        f'<div class="alien-card">'
        f'<div class="alien-svg-box">{alien_art}</div>'
        f'<div class="alien-name">{alien["name"]}</div>'
        f'<div class="alien-type">{alien["power_type"]}</div>'
        f'<div class="alien-planet">🌍 {alien["planet"]}</div>'
        f'{stat_bars}'
        f'<div style="margin-top:8px;font-size:0.8rem;color:#a0a0a0;">Score: {alien["power_score"]}</div>'
        f'</div>'
    )
    return "".join(line.strip() for line in card_html.splitlines())


def get_plotly_dark_green_template():
    """Return a Plotly layout dict for dark green themed charts."""
    return dict(
        template="plotly_dark",
        paper_bgcolor="rgba(10, 15, 10, 0.0)",
        plot_bgcolor="rgba(10, 15, 10, 0.3)",
        font=dict(family="Rajdhani, sans-serif", color="#e0e0e0"),
        title_font=dict(family="Orbitron, sans-serif", color="#39ff14"),
        colorway=[
            "#39ff14", "#1a8a0a", "#66ff66", "#00cc44",
            "#99ff99", "#33cc33", "#00ff88", "#88ff00",
        ],
        xaxis=dict(gridcolor="rgba(57,255,20,0.1)"),
        yaxis=dict(gridcolor="rgba(57,255,20,0.1)"),
    )
