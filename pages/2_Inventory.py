import streamlit as st
import pandas as pd

st.title("📦 Inventory Management")

if "inventory" not in st.session_state:
    st.session_state.inventory = pd.DataFrame(
        columns=["Medicine", "Stock", "Price"]
    )

medicine = st.text_input("Medicine Name")

stock = st.number_input(
    "Stock",
    min_value=0
)

price = st.number_input(
    "Price",
    min_value=0.0
)

if st.button("Add Medicine"):

    new_row = pd.DataFrame({
        "Medicine": [medicine],
        "Stock": [stock],
        "Price": [price]
    })

    st.session_state.inventory = pd.concat(
        [st.session_state.inventory, new_row],
        ignore_index=True
    )

    st.success("Medicine Added Successfully")

st.subheader("Current Inventory")

st.dataframe(
    st.session_state.inventory,
    use_container_width=True
)

