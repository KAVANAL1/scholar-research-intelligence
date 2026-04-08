from agents.search_agent import search_papers
from agents.analysis_agent import analyze_papers
from agents.synthesis_agent import detect_research_gaps


papers = search_papers("machine learning healthcare")

analysis = analyze_papers(papers)

gaps = detect_research_gaps(analysis)

print("\nDetected Research Gaps:\n")

for gap in gaps:
    print("-", gap)
    