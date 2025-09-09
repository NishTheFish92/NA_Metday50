import streamlit as st

RED = "#d32f2f"
LIGHT_GREY = "#f5f5f5"

st.set_page_config(page_title="BP Medicine Advisor", page_icon="💊", layout="centered")
st.markdown(f"""
    <style>
        .reportview-container {{
            background-color: {LIGHT_GREY};
        }}
        .stButton>button {{
            background-color: {RED};
            color: white;
            border-radius: 8px;
            border: none;
            padding: 0.5em 2em;
        }}
        .stTextInput>div>input {{
            border: 2px solid {RED};
            border-radius: 8px;
        }}
    </style>
""", unsafe_allow_html=True)
