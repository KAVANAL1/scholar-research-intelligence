from utils.groq_client import ask_llm


def generate_literature_review(topic, papers, analysis, gaps):

    paper_titles = [

        paper["title"]

        for paper in papers[:6]

    ]

    prompt = f"""

Write a structured literature review for the topic:

{topic}

Use these papers:

{paper_titles}

Output format:

SUMMARY:
(2 sentences describing research area)

COMPARISON:
(compare approaches across papers)

CONTRADICTIONS:
(identify conflicts across methods or datasets)

RESEARCH GAPS:
(list gaps)

FUTURE WORK:
(list improvements researchers should explore)

Return only clean academic text.

"""

    review = ask_llm(prompt)

    return review