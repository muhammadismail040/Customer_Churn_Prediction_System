import streamlit as st

from gauge import probability_gauge

st.title("Gauge Test")

fig = probability_gauge(0.87)

st.plotly_chart(fig, use_container_width=True)