import streamlit as st
import pandas as pd

st.title("📈 Analytics")

sales = pd.DataFrame({
    "Medicine":[
        "Paracetamol",
        "Dolo",
        "Crocin"
    ],
    "Sales":[
        500,
        350,
        250
    ]
})

st.bar_chart(
    sales.set_index(
        "Medicine"
    )
)
