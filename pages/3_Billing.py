import streamlit as st
import pandas as pd

st.title("🧾 Billing")

medicine = st.selectbox(
    "Medicine",
    [
        "Paracetamol",
        "Dolo",
        "Crocin"
    ]
)

qty = st.number_input(
    "Quantity",
    min_value=1
)

price = 10

total = qty * price

st.metric(
    "Total",
    f"₹{total}"
)

if st.button("Generate Bill"):
    st.success(
        "Bill Generated Successfully"
    )
    