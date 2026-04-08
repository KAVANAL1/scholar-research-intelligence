from utils.groq_client import ask_llm


def detect_contradictions(papers):

    if not papers:

        return ["Not enough papers found for contradiction analysis"]

    print("Detecting contradictions between papers...")

    if len(papers) < 2:

        return ["Not enough papers available for comparison"]

    paper_titles = [

        f"Paper {i+1}: {paper['title']}"

        for i, paper in enumerate(papers[:5])

    ]

    paper_text = "\n".join(paper_titles)

    prompt = f"""

Compare the following papers:

{paper_text}

Identify contradictions between:

- datasets used
- evaluation strategies
- modeling approaches
- conclusions

Return 3 concise bullet points referencing Paper numbers.

"""

    response = ask_llm(prompt)

    contradictions = [

        line.replace("-", "").strip()

        for line in response.split("\n")

        if line.strip()

    ]

    print("Contradiction analysis completed")

    return contradictions