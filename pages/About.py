import streamlit as st

from utils.style import apply_custom_style

apply_custom_style()

st.title("About MediInsight AI")

st.write(
    "MediInsight AI is an AI-powered healthcare report analyzer "
    "designed to help users understand information contained in "
    "uploaded medical reports."
)

st.divider()

st.markdown("### What MediInsight AI Does")

st.markdown("""
- Upload medical PDF reports
- Extract text from medical documents
- Store report information using semantic embeddings
- Retrieve relevant medical information using RAG
- Ask questions about the uploaded report
- Generate patient-friendly summaries
- Extract and display laboratory test results
- Identify reported normal, low, and high values
""")

st.markdown("### RAG Architecture")

st.code(
    "Medical PDF\n"
    "    |\n"
    "    v\n"
    "PDF Text Extraction\n"
    "    |\n"
    "    v\n"
    "Document Chunking\n"
    "    |\n"
    "    v\n"
    "Hugging Face Embeddings\n"
    "    |\n"
    "    v\n"
    "ChromaDB Vector Store\n"
    "    |\n"
    "    v\n"
    "Relevant Context Retrieval\n"
    "    |\n"
    "    v\n"
    "Groq LLM\n"
    "    |\n"
    "    v\n"
    "Medical Explanation / Summary"
)

st.markdown("### Technology Stack")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **Frontend**
    
    Streamlit
    """)

with col2:
    st.markdown("""
    **AI / NLP**
    
    Groq LLM  
    Hugging Face Embeddings  
    LangChain
    """)

with col3:
    st.markdown("""
    **Data / Retrieval**
    
    ChromaDB  
    PyMuPDF  
    Python
    """)

st.divider()

st.markdown("### Medical Safety")

st.warning(
    "MediInsight AI is intended for informational and educational purposes. "
    "It explains information contained in uploaded reports but does not "
    "provide medical diagnoses, prescriptions, or treatment decisions. "
    "Users should consult a qualified healthcare professional for medical decisions."
)

st.markdown("### Project")

st.write(
    "MediInsight AI demonstrates the application of Retrieval-Augmented "
    "Generation (RAG), vector databases, embeddings, and large language "
    "models for healthcare document analysis."
)
