"""
vault.py — Alien Vault page.
Displays alien cards in a Pokedex-style grid with filters and search.
"""

import streamlit as st
from utils.helpers import load_alien_data, render_section_title, render_alien_card_html


def show():
    """Render the Alien Vault page."""
    render_section_title("🗃️ ALIEN VAULT")

    df = load_alien_data()

    # --- Filters ---
    col_search, col_type, col_planet, col_sort = st.columns(4)
    with col_search:
        search = st.text_input("🔍 Search", key="vault_search", placeholder="Alien name...")
    with col_type:
        types = ["All"] + sorted(df["power_type"].unique().tolist())
        selected_type = st.selectbox("⚡ Power Type", types, key="vault_type")
    with col_planet:
        planets = ["All"] + sorted(df["planet"].unique().tolist())
        selected_planet = st.selectbox("🌍 Planet", planets, key="vault_planet")
    with col_sort:
        sort_by = st.selectbox("📊 Sort by", ["name", "power_score", "strength", "speed", "defense", "intelligence"], key="vault_sort")

    # Apply filters
    filtered = df.copy()
    if search:
        filtered = filtered[filtered["name"].str.lower().str.contains(search.lower())]
    if selected_type != "All":
        filtered = filtered[filtered["power_type"] == selected_type]
    if selected_planet != "All":
        filtered = filtered[filtered["planet"] == selected_planet]
    filtered = filtered.sort_values(sort_by, ascending=(sort_by == "name"))

    # --- View Toggle ---
    view = st.radio("View mode:", ["🃏 Cards", "📋 Table"], horizontal=True, key="vault_view")

    st.markdown(f"**Showing {len(filtered)} alien(s)**")

    if filtered.empty:
        st.info("No aliens match your filters. Try adjusting your search.")
        return

    if view == "📋 Table":
        # Table view
        st.dataframe(
            filtered[["emoji", "name", "power_type", "planet", "strength", "speed", "defense", "intelligence", "power_score"]],
            use_container_width=True,
            hide_index=True,
        )
    else:
        # Cards view — 3 columns grid
        cols = st.columns(3)
        for idx, (_, alien) in enumerate(filtered.iterrows()):
            with cols[idx % 3]:
                card_html = render_alien_card_html(alien)
                st.markdown(card_html, unsafe_allow_html=True)
