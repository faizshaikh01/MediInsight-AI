from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

from utils.database import get_vector_store


def create_chunks(text, source_name):
    """
    Split document text into smaller chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(text)

    documents = [
        Document(
            page_content=chunk,
            metadata={
                "source": source_name
            }
        )
        for chunk in chunks
    ]

    return documents


def index_document(text, source_name):
    """
    Create chunks and store them in ChromaDB.
    Re-indexing the same document replaces its old chunks.
    """

    documents = create_chunks(
        text,
        source_name
    )

    vector_store = get_vector_store()

    try:
        vector_store.delete(
            where={
                "source": source_name
            }
        )
    except Exception:
        pass

    ids = [
        f"{source_name}_{i}"
        for i in range(len(documents))
    ]

    vector_store.add_documents(
        documents=documents,
        ids=ids
    )

    return len(documents)


def retrieve_documents(query, k=4, source_name=None):
    """
    Retrieve relevant chunks.

    If source_name is provided, retrieve only from
    that specific document.
    """

    vector_store = get_vector_store()

    if source_name:
        documents = vector_store.similarity_search(
            query,
            k=k,
            filter={
                "source": source_name
            }
        )
    else:
        documents = vector_store.similarity_search(
            query,
            k=k
        )

    return documents
