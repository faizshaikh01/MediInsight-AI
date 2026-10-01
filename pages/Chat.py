import streamlit as st

from utils.style import apply_custom_style
from utils.rag import retrieve_documents
from utils.llm import get_llm_response
from utils.prompts import RAG_PROMPT

apply_custom_style()

st.title("Chat with Medical Report")

st.write(
    "Ask questions about your uploaded medical reports."
)

active_document = st.session_state.get(
    "active_document",
    None
)

if active_document:

    st.info(
        f"Active document: {active_document}"
    )

else:

    st.warning(
        "Please upload and index a PDF before asking questions."
    )


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


question = st.chat_input(
    "Ask a question about your report..."
)


if question:

    with st.chat_message("user"):
        st.write(question)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    if not active_document:

        answer = (
            "Please upload and index a PDF before "
            "asking questions."
        )

        documents = []

    else:

        with st.spinner(
            "Searching the medical report..."
        ):

            documents = retrieve_documents(
                question,
                k=4,
                source_name=active_document
            )

        if not documents:

            answer = (
                "I could not find relevant information "
                "in the active medical report."
            )

        else:

            context_parts = []

            # Limit context size to avoid API token limits
            max_context_chars = 10000
            current_chars = 0

            for i, document in enumerate(
                documents,
                1
            ):

                text = document.page_content.strip()

                remaining = (
                    max_context_chars - current_chars
                )

                if remaining <= 0:
                    break

                text = text[:remaining]

                context_parts.append(
                    f"""
SOURCE DOCUMENT: {active_document}

RETRIEVED SECTION {i}:

{text}
"""
                )

                current_chars += len(text)


            context = "\n\n".join(
                context_parts
            )

            prompt = RAG_PROMPT.format(
                context=context,
                question=question
            )

            with st.spinner(
                "Generating answer..."
            ):

                answer = get_llm_response(
                    prompt
                )


    with st.chat_message("assistant"):
        st.write(answer)


    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )


    if documents:

        with st.expander(
            "Retrieved Sources"
        ):

            st.markdown(
                "### Source Document"
            )

            st.write(
                f"**{active_document}**"
            )

            st.markdown(
                "### Retrieved Context"
            )

            for i, document in enumerate(
                documents,
                1
            ):

                st.markdown(
                    f"**Section {i}**"
                )

                st.write(
                    document.page_content
                )
