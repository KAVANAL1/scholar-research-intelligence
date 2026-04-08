from utils.groq_client import ask_llm


def generate_literature_review(topic, papers, analysis, gaps):

    paper_titles = [

    f"Paper {i+1}: {paper.get('title','Unknown')}"

    for i, paper in enumerate(papers[:5])

]

    paper_list_text = "\n".join(paper_titles)

    prompt = f"""

You are an academic research assistant.

Write a structured literature review for the topic:

{topic}

The following papers are analyzed:

{paper_list_text}


Generate output using this format:

SUMMARY OF RESEARCH AREA:
Explain the research domain clearly so readers understand the topic background.

KEY PAPERS ANALYZED:
List Paper 1–Paper 5 with their contributions.

COMPARISON OF PAPERS:
Compare Paper 1 vs Paper 2 vs Paper 3 vs Paper 4 vs Paper 5
based on:
- methodology
- datasets
- performance
- advantages
- limitations

CONTRADICTIONS BETWEEN PAPERS:
Identify differences in approach or conclusions.

RESEARCH GAPS IDENTIFIED:
Explain missing opportunities across these papers.

FUTURE RESEARCH DIRECTIONS:
Suggest improvements researchers should explore.

KNOWLEDGE MAP SUMMARY:
Explain relationships between datasets, methods, and applications
across all papers.

Return clean academic structured text.

"""

    review = ask_llm(prompt)

    return review