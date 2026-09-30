# 📚 ScholAR — Research Intelligence Agent

ScholAR is an AI-powered research assistant that helps users discover and analyze research papers for a given topic.

### 🚀 Live Demo

https://scholar-research-intelligence.onrender.com/

## Features

* 🔎 Research paper search using OpenAlex
* 🧩 Research gap identification
* ⚖️ Contradiction analysis
* 📖 AI-generated literature review
* 🕸️ Knowledge graph visualization

## Tech Stack

**Python · FastAPI · HTML · CSS · JavaScript · Groq API · OpenAlex API**

## Run Locally

```bash
git clone https://github.com/KAVANAL1/scholar-research-intelligence.git
cd scholar-research-intelligence
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

Run:

```bash
uvicorn backend.main:app --reload
```

Open `http://127.0.0.1:8000`

## Project Structure

```text
agents/          → Research and analysis agents
backend/         → FastAPI backend
frontend/        → Web interface
knowledge_graph/ → Knowledge graph generation
```

---

**Built by Kavana L**
