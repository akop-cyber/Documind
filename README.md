# 🧠 Documind — AI-Powered Document Q&A

> Ask questions. Get answers grounded in your document. No hallucinations.

**Live Demo → [docu-mind-ai.netlify.app](https://docu-mind-ai.netlify.app)**

---

## What is Documind?

Documind is a full-stack **Retrieval-Augmented Generation (RAG)** application that lets you upload any PDF and have a real conversation with it. It retrieves only the most relevant chunks from your document, passes them to an LLM, and returns answers that are strictly grounded in the source — refusing to answer when the evidence isn't there. Documind is the productionized evolution of RAG-built-from-scratch-v3 — taking the core retrieval pipeline and wrapping it into a fully deployed web application.

Built entirely from scratch — no LangChain, no LlamaIndex, no high-level RAG frameworks.

---

## How It Works

```
PDF Upload → Text Extraction → Chunking → Embedding → Vector Storage
                                                              ↓
User Query → Embed Query → Cosine Similarity Search → Top Chunks
                                                              ↓
                                              LLM → Grounded Answer
```

Each component is a standalone Python module:

| Module | Role |
|---|---|
| `loader.py` | Extracts raw text from uploaded PDFs |
| `chunker.py` | Splits text into overlapping semantic chunks |
| `embedder.py` | Converts chunks to vectors using `sentence-transformers` |
| `vector.py` | Stores and manages the in-memory vector index |
| `retriever.py` | Finds top-k most relevant chunks via cosine similarity |
| `app.py` | FastAPI backend — handles requests, orchestrates the pipeline |
| `index.html` | Frontend UI with streaming response support |

---

## Features

- 📄 Upload any PDF and query it instantly
- 🔍 Semantic retrieval using `sentence-transformers/all-MiniLM-L6-v2`
- 🚫 Hallucination control — refuses to answer when similarity score falls below threshold
- ⚡ Streaming responses for a real-time chat feel
- 🌐 Fully deployed — backend on Render, frontend on Netlify

---

## Tech Stack

**Backend:** Python, FastAPI, Sentence Transformers, scikit-learn, PyPDF2, NumPy  
**Frontend:** HTML, CSS, JavaScript (vanilla)  
**Deployment:** Render (backend) · Netlify (frontend)

---

## Hallucination Control

If the cosine similarity score of the best-matching chunk is below `0.5`, the system refuses to answer and reports insufficient evidence. This ensures every response is traceable back to the document.

---

## Local Setup

```bash
git clone https://github.com/akop-cyber/Documind.git
cd Documind
pip install -r requirements.txt
uvicorn app:app --reload
```

Then open `index.html` in your browser and point the API URL to `localhost:8000`.

---

## Deployment Architecture

```
Frontend (Netlify)  ──→  Backend API (Render)
     index.html              app.py (FastAPI)
                               ↓
                         RAG Pipeline
                     (loader → chunker → embedder
                      → vector → retriever → LLM)
```

---

## Author

Built by **Aarav Kumar Ranjan** 
[Portfolio](https://aaravkumarranjan.netlify.app) · [GitHub](https://github.com/akop-cyber) · [Kaggle](https://kaggle.com/aaravkumarranjan)

---

*This project does not use LangChain, LlamaIndex, or any external RAG framework. Every component — chunking, embedding, retrieval, similarity scoring — is implemented manually.*
