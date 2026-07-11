import streamlit as st

from sidebar import sidebar

st.set_page_config(
    page_title="Customer Churn Dashboard",
    page_icon="📊",
    layout="wide"
)

page = sidebar()

st.title("📊 Customer Churn Prediction Dashboard")

st.write(f"Current Page: **{page}**")