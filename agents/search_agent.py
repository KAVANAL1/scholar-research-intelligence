import requests


def search_papers(topic):

    print("Searching OpenAlex for:", topic)

    url = "https://api.openalex.org/works"

    params = {
        "search": topic,
        "per-page": 5
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=20
        )

        print("OpenAlex URL:", response.url)
        print("OpenAlex status:", response.status_code)
        print("OpenAlex response:", response.text[:500])

        response.raise_for_status()

        data = response.json()

    except requests.exceptions.RequestException as e:

        print("OpenAlex request failed:", e)

        return []

    except ValueError as e:

        print("OpenAlex returned invalid JSON:", e)

        return []

    papers = []

    for work in data.get("results", []):

        title = work.get("title", "Unknown Title")

        citations = work.get("cited_by_count", 0)

        primary_location = work.get("primary_location") or {}

        paper_url = primary_location.get("landing_page_url")

        pdf_url = primary_location.get("pdf_url")

        abstract = work.get("abstract_inverted_index")

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