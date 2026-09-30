from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from agents.gap_agent import detect_research_gaps
from agents.search_agent import search_papers
from agents.analysis_agent import analyze_papers
from agents.synthesis_agent import detect_contradictions
from agents.review_generator import generate_literature_review
from knowledge_graph.graph_builder import build_knowledge_graph

# Absolute paths so it works no matter where uvicorn is started from
ROOT = Path(__file__).resolve().parent.parent
GRAPH_DIR = ROOT / "knowledge_graph"
FRONTEND_DIR = ROOT / "frontend"
GRAPH_DIR.mkdir(exist_ok=True)   # StaticFiles crashes if the folder is missing

app = FastAPI(title="ScholAR")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.get("/research")
def research(topic: str):
    topic = topic.strip()
    if not topic:
        raise HTTPException(status_code=400, detail="Topic is required.")
    try:
        papers = search_papers(topic)
        analysis = analyze_papers(papers)
        contradictions = detect_contradictions(papers)
        gaps = detect_research_gaps(topic, papers)
        review = generate_literature_review(topic, papers, analysis, gaps)
        build_knowledge_graph(topic, papers, gaps, contradictions)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {
        "topic": topic,
        "papers": papers,
        "gaps": gaps,
        "contradictions": contradictions,
        "review": review,
    }


# Static mounts go LAST so they don't shadow the API routes
app.mount("/graph", StaticFiles(directory=GRAPH_DIR, html=True), name="graph")
app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")
