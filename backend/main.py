from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.planner_agent import run_research_pipeline

app = FastAPI()


# Enable frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "ScholAR Autonomous Research Agent Running"}


@app.get("/research")
def research(topic: str):

    result = run_research_pipeline(topic)

    return {
     "topic": topic,
    "papers_found": len(result["papers"]),
    "papers": result["papers"],
    "gaps": result["gaps"],
    "contradictions": result["contradictions"],
    "review": result["review"]
    }