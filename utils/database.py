import os
import chromadb
from langchain_chroma import Chroma

from utils.embeddings import get_embeddings


VECTOR_DB_PATH = "vector_db"


def get_vector_store():
    embeddings = get_embeddings()

    vector_store = Chroma(
        collection_name="medical_reports",
        embedding_function=embeddings,
        persist_directory=VECTOR_DB_PATH
    )

    return vector_store


def add_documents(chunks):
    vector_store = get_vector_store()

    vector_store.add_documents(chunks)

    return vector_store
