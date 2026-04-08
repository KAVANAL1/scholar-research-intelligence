from agents.search_agent import search_papers
from agents.analysis_agent import analyze_papers
from agents.synthesis_agent import detect_research_gaps
from agents.review_generator import generate_literature_review


topic = "machine learning healthcare"

papers = search_papers(topic)

analysis = analyze_papers(papers)

gaps = detect_research_gaps(analysis)

review = generate_literature_review(
    topic,
    papers,
    analysis,
    gaps
)

print(review)