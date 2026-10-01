import streamlit as st
import os

from utils.parser import extract_text_from_pdf
from utils.rag import index_document


st.title("Upload Medical Report")

st.write(
    "Upload a medical or research PDF to analyze it with MediInsight AI."
)


uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=["pdf"]
)


if uploaded_file is not None:

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(file_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    st.success(
        f"Uploaded: {uploaded_file.name}"
    )

    with st.spinner("Extracting text from PDF..."):

        extracted_text = extract_text_from_pdf(
            file_path
        )

    if extracted_text.strip():

        st.success(
            "PDF text extracted successfully!"
        )

        with st.spinner(
            "Creating embeddings and indexing document..."
        ):

            chunk_count = index_document(
                extracted_text,
                uploaded_file.name
            )

        # Remember the currently selected document
        st.session_state["active_document"] = uploaded_file.name

        st.success(
            f"Document indexed successfully! "
            f"{chunk_count} chunks stored in ChromaDB."
        )

        st.subheader("Extracted Text")

        st.text_area(
            "Document Content",
            extracted_text,
            height=500
        )

    else:

        st.error(
            "No readable text was found in this PDF."
        )
