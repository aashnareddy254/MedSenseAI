import streamlit as st

st.title("🤖 MedSense AI Assistant")

question = st.text_input(
    "Ask a question"
)

if question:

    if "low stock" in question.lower():
        st.write(
            "Paracetamol is running low."
        )

    elif "top selling" in question.lower():
        st.write(
            "Dolo is the top-selling medicine."
        )

    else:
        st.write(
            "I can help with inventory and sales queries."
        )
        