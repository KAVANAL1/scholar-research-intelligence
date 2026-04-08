from agents.search_agent import search_papers
from agents.analysis_agent import analyze_papers
from knowledge_graph.graph_builder import build_graph


papers = search_papers("machine learning healthcare")

analysis = analyze_papers(papers)

build_graph(papers, analysis)