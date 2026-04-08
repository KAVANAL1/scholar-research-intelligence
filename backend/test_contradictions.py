from agents.search_agent import search_papers
from agents.analysis_agent import analyze_papers
from agents.synthesis_agent import detect_contradictions


topic = "machine learning healthcare"

papers = search_papers(topic)

analysis = analyze_papers(papers)

contradictions = detect_contradictions(analysis)


print("\nDetected Contradictions:\n")

for item in contradictions:
    print("-", item)