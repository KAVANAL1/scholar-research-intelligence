<div align="center">

# 📚 ScholAR
### Autonomous Research Intelligence Agent

Type a topic → get papers, research gaps, contradictions & a literature review.

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Open_App-4f46e5?style=for-the-badge)](https://YOUR-APP.onrender.com)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LLM-f55036)

![ScholAR screenshot](docs/screenshot.png)

</div>

## ✨ Features

| | |
|---|---|
| 🔎 **Paper Search** | Top papers with citation counts and links |
| 🧩 **Research Gaps** | What existing studies haven't covered |
| ⚖️ **Contradictions** | Where papers disagree with each other |
| 📖 **Literature Review** | Structured, AI-written synthesis |
| 🕸️ **Knowledge Graph** | Papers, gaps and contradictions in one view |

## 🛠️ Tech Stack

**Backend:** FastAPI · Python  **AI:** Groq API  **Frontend:** HTML · CSS · JavaScript

## ⚡ Run Locally

```bash
git clone https://github.com/KAVANAL1/scholar-research-intelligence.git
cd scholar-research-intelligence
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_key_here
```

```bash
uvicorn backend.main:app --reload
```

Open **http://127.0.0.1:8000** 🎉

## 📁 Structure

```
agents/           🤖 search, analysis, gaps, contradictions, review
backend/          ⚙️ FastAPI app
frontend/         🎨 UI
knowledge_graph/  🕸️ graph builder
```

<div align="center">Made with ❤️ by <a href="https://github.com/KAVANAL1">Kavana L</a></div>
