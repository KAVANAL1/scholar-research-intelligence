from utils.groq_client import ask_llm


def extract_keywords(text):

    text = text.lower()

    keywords = []

    engineering_terms = [

        "sensor",
        "hardware",
        "embedded",
        "measurement",
        "detection",
        "classification",
        "fpga",
        "vlsi",
        "iot",
        "signal processing",
        "circuit",
        "deep learning",
        "machine learning",
        "transformer",
        "cnn",
        "optimization",
        "robotics",
        "control system",
        "image processing",
        "nlp"

    ]

    dataset_terms = [

        "dataset",
        "benchmark",
        "simulation",
        "sensor data",
        "image dataset",
        "training data",
        "test data"

    ]

    limitation_terms = [

        "limited",
        "challenge",
        "latency",
        "hardware limitation",
        "future work",
        "small dataset",
        "scalability"

    ]


    for term in engineering_terms:

        if term in text:

            keywords.append(("method", term))


    for term in dataset_terms:

        if term in text:

            keywords.append(("dataset", term))


    for term in limitation_terms:

        if term in text:

            keywords.append(("limitation", term))


    return keywords



def analyze_papers(papers):

    print("Analyzing papers...")

    analyzed = []

    for paper in papers:

        abstract = paper.get("abstract", "")

        if abstract is None:
            abstract = paper["title"]

        keywords = extract_keywords(abstract)

        analyzed.append({

            "title": paper["title"],
            "keywords": keywords

        })

    print("Analysis completed")

    return analyzed



# 🧠 NEW — Groq-based intelligent research gap detector

def detect_research_gaps(topic, papers):

    paper_titles = [

        paper["title"]

        for paper in papers[:6]

    ]

    prompt = f"""

You are a research assistant.

Based on the research topic:

{topic}

and these papers:

{paper_titles}

Identify 3 research gaps.

Return short bullet points only.

"""

    result = ask_llm(prompt)

    gaps = result.split("\n")

    clean_gaps = [

        gap.replace("-", "").strip()

        for gap in gaps if gap.strip()

    ]

    print("Research gaps detected")

    return clean_gaps