import streamlit as st

st.title("📊 Dashboard")

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Medicines",
    "150"
)

col2.metric(
    "Low Stock",
    "12"
)

col3.metric(
    "Revenue",
    "₹25,000"
)

col4.metric(
    "Alerts",
    "8"
)

st.success(
    "Welcome to MedSense AI Dashboard"
)
