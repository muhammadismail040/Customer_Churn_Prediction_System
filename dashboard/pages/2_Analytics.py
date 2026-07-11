"""
Analytics Dashboard
-------------------
Business analytics and customer insights.
"""

import streamlit as st

from metrics import load_data

from charts import (
    churn_distribution,
    contract_distribution,
    internet_distribution,
    payment_distribution,
    monthly_charge_distribution,
    tenure_distribution,
    tenure_vs_charge,
)

# =====================================

st.set_page_config(
    page_title="Analytics",
    page_icon="📈",
    layout="wide",
)

st.title("📈 Customer Analytics Dashboard")

df = load_data()

# =====================================
# Row 1
# =====================================

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        churn_distribution(df),
        use_container_width=True,
    )

with col2:
    st.plotly_chart(
        contract_distribution(df),
        use_container_width=True,
    )

# =====================================
# Row 2
# =====================================

col3, col4 = st.columns(2)

with col3:
    st.plotly_chart(
        internet_distribution(df),
        use_container_width=True,
    )

with col4:
    st.plotly_chart(
        payment_distribution(df),
        use_container_width=True,
    )

# =====================================
# Row 3
# =====================================

col5, col6 = st.columns(2)

with col5:
    st.plotly_chart(
        monthly_charge_distribution(df),
        use_container_width=True,
    )

with col6:
    st.plotly_chart(
        tenure_distribution(df),
        use_container_width=True,
    )

# =====================================
# Row 4
# =====================================

st.plotly_chart(
    tenure_vs_charge(df),
    use_container_width=True,
)

st.success("✅ Analytics Dashboard Loaded Successfully")