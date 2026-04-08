# database/schema.py

class ResearchResult:
    def __init__(self, papers, graph, summary):
        self.papers = papers
        self.graph = graph
        self.summary = summary