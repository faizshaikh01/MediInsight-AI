import streamlit as st

def apply_custom_style():
    st.markdown("""
    <style>
    .stApp {
        background:
            radial-gradient(circle at 10% 10%, rgba(20,184,166,.12), transparent 30%),
            radial-gradient(circle at 90% 10%, rgba(99,102,241,.12), transparent 30%),
            #0f172a;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #111827, #0f172a);
        border-right: 1px solid rgba(148,163,184,.15);
    }

    h1 {
        font-weight: 800 !important;
        letter-spacing: -1px;
    }

    h2, h3 {
        font-weight: 700 !important;
    }

    .stButton > button {
        border-radius: 10px;
        border: 1px solid rgba(45,212,191,.35);
        background: linear-gradient(135deg, #0d9488, #2563eb);
        color: white;
        font-weight: 600;
        transition: .2s;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(37,99,235,.25);
    }

    [data-testid="stMetric"] {
        background: rgba(30,41,59,.75);
        border: 1px solid rgba(148,163,184,.15);
        border-radius: 16px;
        padding: 18px;
    }

    [data-testid="stFileUploader"] {
        background: rgba(30,41,59,.55);
        border: 1px dashed rgba(45,212,191,.45);
        border-radius: 16px;
    }

    [data-testid="stChatMessage"] {
        border-radius: 14px;
        margin-bottom: 12px;
    }

    [data-testid="stExpander"] {
        border: 1px solid rgba(148,163,184,.15);
        border-radius: 14px;
        background: rgba(30,41,59,.45);
    }

    [data-testid="stAlert"] {
        border-radius: 12px;
    }

    hr {
        border-color: rgba(148,163,184,.15);
    }
    </style>
    """, unsafe_allow_html=True)

