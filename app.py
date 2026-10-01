import streamlit as st
from utils.style import apply_custom_style

st.set_page_config(
    page_title="MediInsight AI",
    page_icon="AI",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_custom_style()

with st.sidebar:
    st.markdown("## MediInsight AI")
    st.caption("Healthcare Report Intelligence")
    st.divider()
    st.success("System Online")
    st.markdown("### Technology")
    st.markdown("""
**GenAI**

**RAG Pipeline**

**ChromaDB**

**Groq LLM**

**Hugging Face Embeddings**
""")

st.markdown("""
<div style="background:linear-gradient(135deg,#0f766e,#1e3a8a);padding:45px;border-radius:24px;margin-bottom:30px;">
<div style="font-size:18px;color:#99f6e4;font-weight:700;margin-bottom:12px;">
AI-POWERED HEALTHCARE INTELLIGENCE
</div>
<h1 style="font-size:52px;color:white;margin:0;">
MediInsight AI
</h1>
<p style="font-size:21px;color:#dbeafe;margin-top:18px;line-height:1.6;">
Analyze healthcare reports, retrieve relevant information,
ask questions, and generate intelligent summaries using
Retrieval-Augmented Generation.
</p>
</div>
""", unsafe_allow_html=True)

st.subheader("What can you do?")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("### Upload")
    st.markdown("**Report Analysis**")
    st.caption("Upload PDF healthcare reports and extract their content.")

with col2:
    st.markdown("### Search")
    st.markdown("**Semantic Retrieval**")
    st.caption("Find relevant information using vector similarity search.")

with col3:
    st.markdown("### Chat")
    st.markdown("**Document Q&A**")
    st.caption("Ask questions about uploaded reports using RAG.")

with col4:
    st.markdown("### Summary")
    st.markdown("**AI Summarization**")
    st.caption("Generate concise summaries from healthcare documents.")

st.divider()

st.subheader("RAG Architecture")

st.markdown("""
<div style="text-align:center;padding:25px;background:#111827;border-radius:18px;">
<span style="padding:12px 18px;background:#1e293b;border-radius:10px;">PDF</span>
<span style="font-size:25px;color:#5eead4;">  </span>
<span style="padding:12px 18px;background:#1e293b;border-radius:10px;">Text Extraction</span>
<span style="font-size:25px;color:#5eead4;">  </span>
<span style="padding:12px 18px;background:#1e293b;border-radius:10px;">Chunking</span>
<span style="font-size:25px;color:#5eead4;">  </span>
<span style="padding:12px 18px;background:#1e293b;border-radius:10px;">Embeddings</span>
<span style="font-size:25px;color:#5eead4;">  </span>
<span style="padding:12px 18px;background:#1e293b;border-radius:10px;">ChromaDB</span>
<span style="font-size:25px;color:#5eead4;">  </span>
<span style="padding:12px 18px;background:#1e293b;border-radius:10px;">Groq LLM</span>
</div>
""", unsafe_allow_html=True)

st.divider()

st.subheader("Technical Stack")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("**Frontend**")
    st.write("Streamlit")

with c2:
    st.markdown("**AI / RAG**")
    st.write("LangChain | Hugging Face | ChromaDB")

with c3:
    st.markdown("**LLM**")
    st.write("Groq API")

st.divider()

st.info(
    "MediInsight AI is an educational document-analysis system. "
    "It does not provide medical diagnosis or replace professional healthcare advice."
)

st.caption("MediInsight AI | GenAI + RAG Healthcare Document Intelligence")


