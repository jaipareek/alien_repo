"""
data_lab.py — Data Lab page.
Upload CSV files, preview data, generate automatic charts.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
from utils.helpers import render_section_title, get_plotly_dark_green_template


def show():
    """Render the Data Lab page."""
    render_section_title("🧪 DATA LAB — CSV Analyzer")

    st.markdown(
        '<p style="color:#a0a0a0;">Upload any CSV file to preview, analyze, and visualize your data.</p>',
        unsafe_allow_html=True,
    )

    uploaded = st.file_uploader(
        "Drop your CSV file here",
        type=["csv"],
        key="datalab_upload",
    )

    if uploaded is None:
        st.info("📂 Upload a CSV file to get started.")
        return

    # Try to read the file
    try:
        df = pd.read_csv(uploaded)
    except Exception as e:
        st.error(f"❌ Could not read this file: {e}")
        return

    if df.empty:
        st.warning("⚠️ The uploaded file is empty.")
        return

    # --- Preview ---
    render_section_title("📋 DATA PREVIEW")
    st.dataframe(df.head(20), use_container_width=True, hide_index=True)

    # --- Info Row ---
    i1, i2, i3 = st.columns(3)
    with i1:
        st.metric("Rows", df.shape[0])
    with i2:
        st.metric("Columns", df.shape[1])
    with i3:
        st.metric("Missing Values", int(df.isnull().sum().sum()))

    # --- Column Types ---
    with st.expander("📐 Column Types"):
        st.dataframe(
            df.dtypes.reset_index().rename(columns={"index": "Column", 0: "Type"}),
            use_container_width=True,
            hide_index=True,
        )

    # --- Describe ---
    with st.expander("📊 Statistical Summary (describe)"):
        st.dataframe(df.describe(), use_container_width=True)

    # --- Chart Builder ---
    render_section_title("📈 CHART BUILDER")

    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    all_cols = df.columns.tolist()

    if not numeric_cols:
        st.warning("No numeric columns found for charting.")
    else:
        cc1, cc2, cc3 = st.columns(3)
        with cc1:
            chart_type = st.selectbox(
                "Chart type",
                ["Bar", "Line", "Scatter", "Histogram", "Box"],
                key="datalab_chart_type",
            )
        with cc2:
            x_col = st.selectbox("X-axis", all_cols, key="datalab_x")
        with cc3:
            y_col = st.selectbox("Y-axis", numeric_cols, key="datalab_y")

        theme = get_plotly_dark_green_template()

        try:
            if chart_type == "Bar":
                fig = px.bar(df, x=x_col, y=y_col, title=f"{y_col} by {x_col}", color_discrete_sequence=["#39ff14"])
            elif chart_type == "Line":
                fig = px.line(df, x=x_col, y=y_col, title=f"{y_col} vs {x_col}", color_discrete_sequence=["#39ff14"])
            elif chart_type == "Scatter":
                fig = px.scatter(df, x=x_col, y=y_col, title=f"{y_col} vs {x_col}", color_discrete_sequence=["#39ff14"])
            elif chart_type == "Histogram":
                fig = px.histogram(df, x=y_col, title=f"Distribution of {y_col}", color_discrete_sequence=["#39ff14"])
            else:  # Box
                fig = px.box(df, x=x_col, y=y_col, title=f"Boxplot of {y_col} grouped by {x_col}", color_discrete_sequence=["#39ff14"])

            fig.update_layout(**theme, height=420)
            st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.error(f"❌ Could not render chart: {e}")

    # --- Download ---
    st.markdown("---")
    csv_data = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇️ Download Data as CSV",
        data=csv_data,
        file_name="omnitrix_lab_export.csv",
        mime="text/csv",
        key="datalab_download",
    )
