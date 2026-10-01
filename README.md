\# MediInsight AI



\## AI-Powered Healthcare Report Analyzer using RAG



MediInsight AI is an AI-powered healthcare document analysis application that uses \*\*Retrieval-Augmented Generation (RAG)\*\* to analyze medical PDF reports and provide grounded answers, structured summaries, and laboratory insights.



The system combines \*\*Python, Streamlit, LangChain, Hugging Face Embeddings, ChromaDB, Groq LLM, and PyMuPDF\*\* to build an end-to-end document intelligence pipeline.



\---



\## Key Features



\- Upload medical PDF reports

\- Extract text from PDF documents

\- Split documents into semantic chunks

\- Generate vector embeddings using Hugging Face

\- Store embeddings in ChromaDB

\- Retrieve relevant medical information using RAG

\- Chat with uploaded medical reports

\- Generate structured report summaries

\- Extract laboratory test results

\- Display normal, low, and high test values

\- Active-document filtering for accurate retrieval

\- Patient-friendly explanations

\- Medical safety disclaimer



\---



\## System Architecture



```text

&#x20;                   Medical PDF Report

&#x20;                          |

&#x20;                          v

&#x20;                 PDF Text Extraction

&#x20;                      PyMuPDF

&#x20;                          |

&#x20;                          v

&#x20;                 Document Chunking

&#x20;               LangChain Text Splitter

&#x20;                          |

&#x20;                          v

&#x20;                 Embedding Generation

&#x20;            Hugging Face Sentence Transformer

&#x20;                          |

&#x20;                          v

&#x20;                   ChromaDB

&#x20;                 Vector Database

&#x20;                          |

&#x20;                          v

&#x20;                 Similarity Retrieval

&#x20;                          |

&#x20;                          v

&#x20;                 Relevant Context

&#x20;                          |

&#x20;                          v

&#x20;                    Groq LLM

&#x20;                          |

&#x20;                          v

&#x20;             Grounded AI Response

&#x20;                          |

&#x20;            +-------------+-------------+

&#x20;            |             |             |

&#x20;            v             v             v

&#x20;          Chat         Summary      Dashboard

```



\---



\## Technology Stack



\### Programming

\- Python 3.10



\### Frontend

\- Streamlit



\### Generative AI

\- Groq API

\- `openai/gpt-oss-20b`



\### RAG / NLP

\- LangChain

\- Retrieval-Augmented Generation

\- Hugging Face Sentence Transformers

\- `all-MiniLM-L6-v2`



\### Vector Database

\- ChromaDB



\### Document Processing

\- PyMuPDF



\### Environment Management

\- Python Virtual Environment

\- python-dotenv



\---



\## Project Structure



```text

MediInsight-AI/

│

├── app.py

├── README.md

├── requirements.txt

├── .gitignore

│

├── assets/

│

├── pages/

│   ├── About.py

│   ├── Chat.py

│   ├── Dashboard.py

│   ├── Summary.py

│   └── Upload\_Report.py

│

├── utils/

│   ├── database.py

│   ├── embeddings.py

│   ├── llm.py

│   ├── medical.py

│   ├── parser.py

│   ├── prompts.py

│   ├── rag.py

│   └── style.py

│

├── uploads/

├── vector\_db/

├── chat\_history/

└── venv/

```



`uploads/`, `vector\_db/`, `chat\_history/`, and `venv/` are excluded from Git using `.gitignore`.



\---



\## Application Workflow



\### 1. Upload Report



The user uploads a medical PDF report through the Streamlit interface.



\### 2. Text Extraction



PyMuPDF extracts text from the uploaded PDF.



\### 3. Document Chunking



The extracted text is divided into smaller overlapping chunks using LangChain's `RecursiveCharacterTextSplitter`.



\### 4. Embedding Generation



Each document chunk is converted into a numerical vector using the Hugging Face embedding model:



```text

sentence-transformers/all-MiniLM-L6-v2

```



\### 5. Vector Storage



The generated embeddings are stored in \*\*ChromaDB\*\*.



\### 6. Retrieval



When the user asks a question, the system performs semantic similarity search and retrieves relevant sections from the active document.



\### 7. LLM Generation



The retrieved context is passed to the Groq-hosted LLM.



The model generates an answer using the retrieved document context instead of relying only on general model knowledge.



\### 8. Output



The application provides:



\- Question answering

\- Report summaries

\- Laboratory analysis

\- Dashboard-based insights



\---



\## RAG Implementation



The project follows the basic RAG pipeline:



```text

Document

&#x20;  ↓

Chunking

&#x20;  ↓

Embeddings

&#x20;  ↓

Vector Database

&#x20;  ↓

Similarity Search

&#x20;  ↓

Relevant Context

&#x20;  ↓

LLM

&#x20;  ↓

Grounded Response

```



The system also applies \*\*active-document filtering\*\*, which helps prevent information from another uploaded document from being retrieved when the user is asking about the currently selected report.



\---



\## Main Application Pages



\### Upload Report



Upload and index medical PDF reports into the RAG pipeline.



\### Chat



Ask questions about the active medical report and receive context-grounded responses.



\### Summary



Generate a structured summary containing sections such as:



\- Overview

\- Objective

\- Methodology

\- Main Components

\- Key Findings

\- Conclusion

\- Limitations



\### Dashboard



Extract and display laboratory test information including:



\- Test name

\- Result

\- Unit

\- Reference range

\- Status



\### About



Provides information about the project, architecture, technology stack, and medical safety considerations.



\---



\## Installation



Clone the repository:



```bash

git clone https://github.com/faizshaikh01/MediInsight-AI.git

```



Navigate to the project:



```bash

cd MediInsight-AI

```



Create a virtual environment:



```bash

python -m venv venv

```



Activate the environment on Windows PowerShell:



```powershell

.\\venv\\Scripts\\Activate.ps1

```



Install dependencies:



```powershell

pip install -r requirements.txt

```



\---



\## Environment Variables



Create a `.env` file in the project root:



```text

GROQ\_API\_KEY=your\_groq\_api\_key

```



The `.env` file is intentionally excluded from Git.



\*\*Never commit or publicly expose your API key.\*\*



\---



\## Run the Application



Start the Streamlit application:



```powershell

streamlit run app.py

```



The application will open in your browser at the local Streamlit address.



\---



\## Medical Safety



MediInsight AI is designed for \*\*educational and informational purposes\*\*.



The application analyzes information contained in uploaded documents and does not provide medical diagnosis, prescriptions, or treatment decisions.



Medical information should be reviewed with a qualified healthcare professional before making healthcare decisions.



\---



\## Future Improvements



\- OCR support for scanned medical reports

\- Improved medical table extraction

\- Multi-report comparison

\- Medical entity extraction

\- Report history

\- Patient profile management

\- Support for additional document formats

\- Improved citation and evidence tracking

\- Multimodal medical document analysis



\---



\## Author



\*\*Md Faiz Alam\*\*



M.Tech — Computer Science \& Engineering



NIT Jalandhar



GitHub: https://github.com/faizshaikh01



\---



\## Disclaimer



This project is an academic and portfolio project intended for educational and informational purposes only. It is not a medical diagnostic system and should not be used as a substitute for professional medical advice, diagnosis, or treatment.

