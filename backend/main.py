from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agents.gap_agent import detect_research_gaps
from agents.search_agent import search_papers
from agents.analysis_agent import analyze_papers
from agents.synthesis_agent import detect_contradictions
from agents.review_generator import generate_literature_review
from knowledge_graph.graph_builder import build_graph

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "ScholAR Autonomous Research Agent Running"
    }


@app.get("/research")
def research(topic: str):

    papers = search_papers(topic)

    analysis = analyze_papers(papers)

    contradictions = detect_contradictions(papers)

    gaps = detect_research_gaps(topic, papers)

    review = generate_literature_review(

        topic,

        papers,

        analysis,

        gaps
    )

    build_graph(topic, papers, contradictions, gaps)

    return {

        "topic": topic,

        "papers": papers,

        "gaps": gaps,

        "contradictions": contradictions,

        "review": review

    }