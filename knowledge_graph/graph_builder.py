from pyvis.network import Network
import networkx as nx
import os


def build_graph(papers, analysis):

    print("Building intelligent knowledge graph...")

    G = nx.Graph()

    for paper in papers:

        paper_title = paper["title"]

        G.add_node(paper_title, color="blue")

        for item in analysis:

            if item["title"] == paper_title:

                for keyword_type, keyword_value in item["keywords"]:

                    keyword_node = f"{keyword_type}: {keyword_value}"

                    G.add_node(keyword_node, color="green")

                    G.add_edge(paper_title, keyword_node)

    net = Network(height="750px", width="100%")

    net.from_nx(G)

    output_path = os.path.join(
        os.getcwd(),
        "knowledge_graph",
        "graph.html"
    )

    net.write_html(output_path)

    print("Smart graph saved at:", output_path)