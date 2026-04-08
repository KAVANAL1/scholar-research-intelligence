from agents.search_agent import search_papers


papers = search_papers("machine learning healthcare")

print("\nRESULTS:\n")

for paper in papers:
    print(paper["title"])