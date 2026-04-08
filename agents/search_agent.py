import requests


def search_papers(topic):

    print("Searching OpenAlex for:", topic)

    url = f"https://api.openalex.org/works?search={topic}&per-page=6"

    response = requests.get(url)

    data = response.json()

    papers = []

    for work in data["results"]:

        title = work.get("title", "No title")

        citations = work.get("cited_by_count", 0)

        paper_url = work.get("primary_location", {}).get("landing_page_url")

        pdf_url = work.get("primary_location", {}).get("pdf_url")

        papers.append({

            "title": title,

            "citations": citations,

            "url": paper_url,

            "pdf": pdf_url

        })

    papers = sorted(

        papers,

        key=lambda x: x["citations"],

        reverse=True

    )

    print("Number of papers found:", len(papers))

    return papers