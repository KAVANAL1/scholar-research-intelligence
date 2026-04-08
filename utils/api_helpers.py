# utils/api_helpers.py

def format_response(papers, graph, summary):
    return {
        "papers": papers,
        "graph": graph,
        "summary": summary
    }