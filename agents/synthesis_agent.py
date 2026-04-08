from utils.groq_client import ask_llm


def detect_contradictions(papers):

    print("Detecting contradictions between papers...")

    if not papers:
        return ["Not enough papers available for contradiction analysis"]

    paper_titles = [

        paper["title"]

        for paper in papers[:6]

    ]

    prompt = f"""

You are an academic research analyst.

Compare the following research papers:

{paper_titles}

Identify contradictions between:

- methodology
- datasets used
- evaluation techniques
- conclusions

Return 2 short bullet points.

If no contradiction exists, suggest comparison opportunities.

Only return bullet points.

"""

    response = ask_llm(prompt)

    contradictions = [

        line.replace("-", "").strip()

        for line in response.split("\n")

        if line.strip()

    ]

    print("Contradiction analysis completed")

    return contradictions