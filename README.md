# ScholAR – Autonomous Research Intelligence Agent

ScholAR is an AI-powered system that automatically:

• Searches academic research papers
• Builds semantic knowledge graphs
• Detects research gaps
• Identifies contradictions
• Generates literature review reports

Backend:
FastAPI + Python

Visualization:
NetworkX + PyVis

Run backend:

uvicorn backend.main:app --reload

Open browser:

http://127.0.0.1:8000/research?topic=AI