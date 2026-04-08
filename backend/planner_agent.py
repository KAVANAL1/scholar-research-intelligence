from agents.search_agent import search_papers
from agents.analysis_agent import analyze_papers
from agents.analysis_agent import detect_research_gaps
from agents.synthesis_agent import detect_contradictions
from agents.review_generator import generate_literature_review
from knowledge_graph.graph_builder import build_graph


def run_research_pipeline(topic):

    print("\nStarting autonomous research pipeline...\n")


    # Step 1: Search papers
    papers = search_papers(topic)


    # Step 2: Analyze papers
    analysis = analyze_papers(papers)


    # Step 3: Build knowledge graph
    build_graph(papers, analysis)


    # Step 4: Detect research gaps
    gaps = detect_research_gaps(topic, papers)


    # Step 5: Detect contradictions
    contradictions = detect_contradictions(papers)


    # Step 6: Generate literature review
    review = generate_literature_review(
        topic,
        papers,
        analysis,
        gaps
    )


    return {
        "papers": papers,
        "analysis": analysis,
        "gaps": gaps,
        "contradictions": contradictions,
        "review": review
    }