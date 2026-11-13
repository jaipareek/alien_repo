"""
analytics.py — Analytics Dashboard page.
Interactive Plotly charts with KPI cards and alien comparisons.
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from utils.helpers import (
    load_alien_data,
    render_section_title,
    render_kpi_card,
    get_plotly_dark_green_template,
)


def show():
    """Render the Analytics Dashboard page."""
    render_section_title("📊 ANALYTICS DASHBOARD")

    df = load_alien_data()
    theme = get_plotly_dark_green_template()

    # --- KPI Row ---
    total = len(df)
    avg_power = round(df["power_score"].mean(), 1)
    strongest = df.loc[df["strength"].idxmax(), "name"]
    fastest = df.loc[df["speed"].idxmax(), "name"]

    k1, k2, k3, k4 = st.columns(4)
    with k1:
        st.markdown(render_kpi_card("Total Aliens", total), unsafe_allow_html=True)
    with k2:
        st.markdown(render_kpi_card("Avg Power Score", avg_power), unsafe_allow_html=True)
    with k3:
        st.markdown(render_kpi_card("Strongest", f"💪 {strongest}"), unsafe_allow_html=True)
    with k4:
        st.markdown(render_kpi_card("Fastest", f"⚡ {fastest}"), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- Row 1: Bar + Donut ---
    c1, c2 = st.columns(2)

    with c1:
        fig_bar = px.bar(
            df.sort_values("power_score", ascending=True),
            x="power_score", y="name", orientation="h",
            title="Power Score by Alien",
            text="power_score",
            color="power_score",
            color_continuous_scale=["#1a8a0a", "#39ff14", "#bbffbb"],
        )
        fig_bar.update_layout(**theme, showlegend=False, height=450)
        fig_bar.update_traces(textposition="outside")
        st.plotly_chart(fig_bar, use_container_width=True)

    with c2:
        type_counts = df["power_type"].value_counts().reset_index()
        type_counts.columns = ["power_type", "count"]
        fig_donut = px.pie(
            type_counts, values="count", names="power_type",
            title="Aliens by Power Type", hole=0.45,
        )
        fig_donut.update_layout(**theme, height=450)
        fig_donut.update_traces(
            textposition="inside", textinfo="label+value",
            marker=dict(line=dict(color="#0a0f0a", width=2)),
        )
        st.plotly_chart(fig_donut, use_container_width=True)

    # --- Row 2: Scatter + Histogram ---
    c3, c4 = st.columns(2)

    with c3:
        fig_scatter = px.scatter(
            df, x="strength", y="speed", size="power_score",
            color="power_type", hover_name="name",
            title="Strength vs Speed",
            text="emoji",
        )
        fig_scatter.update_layout(**theme, height=420)
        fig_scatter.update_traces(textposition="top center", textfont_size=16)
        st.plotly_chart(fig_scatter, use_container_width=True)

    with c4:
        fig_hist = px.histogram(
            df, x="power_score", nbins=8,
            title="Power Score Distribution",
            color_discrete_sequence=["#39ff14"],
        )
        fig_hist.update_layout(**theme, height=420, bargap=0.15)
        st.plotly_chart(fig_hist, use_container_width=True)

    # --- Radar Chart: Compare Aliens ---
    render_section_title("🕸️ COMPARE ALIENS (RADAR)")

    compare_aliens = st.multiselect(
        "Select 2–3 aliens to compare:",
        df["name"].tolist(),
        default=df["name"].tolist()[:2],
        max_selections=3,
        key="analytics_compare",
    )

    if compare_aliens:
        categories = ["strength", "speed", "defense", "intelligence"]
        fig_radar = go.Figure()

        colors = ["#39ff14", "#00ccff", "#ff6644"]
        fill_colors = ["rgba(57, 255, 20, 0.25)", "rgba(0, 204, 255, 0.25)", "rgba(255, 102, 68, 0.25)"]
        for i, alien_name in enumerate(compare_aliens):
            alien = df[df["name"] == alien_name].iloc[0]
            values = [alien[c] for c in categories] + [alien[categories[0]]]  # close the loop
            fig_radar.add_trace(go.Scatterpolar(
                r=values,
                theta=categories + [categories[0]],
                fill="toself",
                name=alien_name,
                line=dict(color=colors[i % len(colors)], width=2),
                fillcolor=fill_colors[i % len(fill_colors)],
                opacity=0.85,
            ))

        fig_radar.update_layout(
            polar=dict(
                bgcolor="rgba(10,15,10,0.3)",
                radialaxis=dict(visible=True, range=[0, 100], gridcolor="rgba(57,255,20,0.15)"),
                angularaxis=dict(gridcolor="rgba(57,255,20,0.15)"),
            ),
            title="Alien Stat Comparison",
            height=480,
            **{k: v for k, v in theme.items() if k != "xaxis" and k != "yaxis"},
        )
        st.plotly_chart(fig_radar, use_container_width=True)
    else:
        st.info("Select at least one alien to see the radar chart.")
