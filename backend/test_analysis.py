from agents.search_agent import search_papers
from agents.analysis_agent import analyze_papers


papers = search_papers("machine learning healthcare")

analysis = analyze_papers(papers)

for item in analysis:
    print(item)