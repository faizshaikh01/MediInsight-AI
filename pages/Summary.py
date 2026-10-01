import streamlit as st

from utils.style import apply_custom_style
from utils.rag import retrieve_documents
from utils.llm import get_llm_response
from utils.prompts import SUMMARY_PROMPT

apply_custom_style()

st.title("Document Summary")

st.write(
    "Generate a structured AI summary of the active document."
)


# Get active document
active_document = st.session_state.get(
    "active_document",
    None
)


if not active_document:

    st.warning(
        "Please upload and index a PDF before generating a summary."
    )

    st.stop()


st.info(
    f"Active document: {active_document}"
)


if st.button(
    "Generate Summary",
    use_container_width=True
):

    with st.spinner(
        "Retrieving important sections from the document..."
    ):

        search_queries = [
            "abstract objective problem motivation",
            "methodology architecture framework system design components",
            "experiments evaluation results findings performance",
            "discussion conclusion contributions",
            "limitations challenges future work"
        ]

        all_documents = []

        seen_content = set()

        for query in search_queries:

            documents = retrieve_documents(
                query,
                k=3,
                source_name=active_document
            )

            for document in documents:

                content = document.page_content.strip()

                if content and content not in seen_content:

                    seen_content.add(content)

                    all_documents.append(document)


        # Keep context within a reasonable size
        all_documents = all_documents[:15]


    if not all_documents:

        st.error(
            "Could not retrieve relevant information from the active document."
        )

        st.stop()


    # Build context
    context_parts = []

    for i, document in enumerate(
        all_documents,
        1
    ):

        source = document.metadata.get(
            "source",
            active_document
        )

        context_parts.append(
            f"""
SOURCE DOCUMENT: {source}

SECTION {i}:

{document.page_content}
"""
        )


    context = "\n\n".join(
        context_parts
    )


    # Generate summary
    prompt = SUMMARY_PROMPT.format(
        context=context
    )


    with st.spinner(
        "Generating structured summary..."
    ):

        summary = get_llm_response(
            prompt
        )


    st.success(
        "Summary generated successfully."
    )


    st.markdown(
        summary
    )


    # Retrieved source information
    with st.expander(
        "Retrieved Source Sections"
    ):

        st.write(
            f"Retrieved {len(all_documents)} relevant sections "
            f"from the active document."
        )

        for i, document in enumerate(
            all_documents,
            1
        ):

            st.markdown(
                f"### Section {i}"
            )

            st.write(
                document.page_content
            )
