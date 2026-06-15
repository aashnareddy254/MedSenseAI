import streamlit as st
import pandas as pd

st.title("📦 Inventory Management")

medicine = st.text_input(
    "Medicine Name"
)

stock = st.number_input(
    "Stock",
    min_value=0
)

price = st.number_input(
    "Price",
    min_value=0.0
)

if st.button("Add Medicine"):
    st.success(
        f"{medicine} added successfully"
    )

sample_data = pd.DataFrame({
    "Medicine":[
        "Paracetamol",
        "Dolo",
        "Crocin"
    ],
    "Stock":[
        100,
        45,
        20
    ],
    "Price":[
        5,
        8,
        10
    ]
})

st.dataframe(
    sample_data,
    use_container_width=True
)
