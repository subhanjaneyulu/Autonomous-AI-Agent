# Autonomous AI Document Generator

## Overview

This project is an Autonomous AI Agent that converts a natural language request into a professional Microsoft Word (.docx) document. The agent automatically understands the user's request, creates an execution plan, performs the required tasks, reviews the generated content, and finally produces a polished business document.

The project is built using Python, FastAPI, Streamlit, LangChain, and Groq LLM.

---

## Features

- Accepts natural language user requests
- Generates its own execution plan
- Performs autonomous multi-step task planning
- Creates professional business documents
- Reviews the generated document using AI Reflection
- Generates Microsoft Word (.docx) documents
- REST API built with FastAPI
- Interactive user interface using Streamlit
- Uses Groq (Llama 3.3 70B) for fast AI inference

---

## Project Workflow

User Request
↓
Planner
↓
Execution Plan
↓
Executor
↓
Document Generation
↓
Reflection / Self Check
↓
DOCX Generator
↓
Final Word Document

---

## Tech Stack

- Python
- FastAPI
- Streamlit
- LangChain
- Groq (Llama 3.3 70B Versatile)
- Pydantic
- Python-docx
- UV Package Manager

---

## Project Structure

```
project/
│
├── api.py
├── app.py
├── config.py
├── models.py
├── prompts.py
├── planner.py
├── executor.py
├── reflection.py
├── doc_generator.py
├── output/
├── requirements.txt
└── README.md
```

---

## Installation

```bash
git clone <repository-url>

cd project

uv sync
```

Create a `.env` file

```
GROQ_API_KEY=your_api_key
```

---

## Run FastAPI

```bash
uv run uvicorn api:app --reload
```

Swagger API

```
http://127.0.0.1:8000/docs
```

---

## Run Streamlit

```bash
uv run streamlit run app.py
```

---

## API Endpoint

### POST /agent

Request

```json
{
  "request": "Create a business proposal for an AI based Hospital Management System."
}
```

Response

```json
{
  "status": "success",
  "review": "APPROVED",
  "execution_plan": "...",
  "document": "...",
  "document_path": "output/Business_Proposal.docx"
}
```

---

## Engineering Improvement

This project implements **Reflection / Self-Check** as its engineering improvement.

After generating the document, the AI agent performs a quality review to verify the document structure, completeness, and professional formatting before producing the final output.

---

## Future Improvements

- Conversation Memory
- RAG Integration
- Tool Calling
- Multi-Agent Architecture
- Cloud Storage Integration
- PDF Export Support

---

## Author

Developed by **Subhanjaneyulu Kallagandla**
