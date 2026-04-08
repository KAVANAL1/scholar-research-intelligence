from utils.groq_client import ask_llm


def detect_research_gaps(topic, papers):

    if not papers:

        return ["Not enough papers found to identify research gaps"]

    paper_titles = [

        f"Paper {i+1}: {paper['title']}"

        for i, paper in enumerate(papers[:5])

    ]

    paper_text = "\n".join(paper_titles)

    prompt = f"""

You are an academic research analyst.

Topic:
{topic}

Papers analyzed:
{paper_text}

Identify 3 meaningful research gaps based on these papers.

Return only short bullet points.

"""

    response = ask_llm(prompt)

    gaps = [

        line.replace("-", "").strip()

        for line in response.split("\n")

        if line.strip()

    ]

    return gaps