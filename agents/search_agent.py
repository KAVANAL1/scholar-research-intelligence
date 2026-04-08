import requests


def search_papers(topic):

    print("Searching OpenAlex for:", topic)

    url = f"https://api.openalex.org/works?search={topic}&per-page=5"

    response = requests.get(url)

    data = response.json()

    papers = []

    for work in data.get("results", []):

        title = work.get("title", "Unknown Title")

        citations = work.get("cited_by_count", 0)

        primary_location = work.get("primary_location") or {}

        paper_url = primary_location.get("landing_page_url")

        pdf_url = primary_location.get("pdf_url")

        abstract = work.get("abstract_inverted_index")

        # Convert OpenAlex abstract format safely

        if abstract:

            abstract = " ".join(

                sorted(

                    abstract,

                    key=lambda x: abstract[x][0]

                )

            )

        else:

            abstract = ""

        papers.append({

            "title": title,

            "citations": citations,

            "url": paper_url,

            "pdf": pdf_url,

            "abstract": abstract

        })

    papers = sorted(

        papers,

        key=lambda x: x["citations"],

        reverse=True

    )

    print("Number of papers found:", len(papers))

    return papers