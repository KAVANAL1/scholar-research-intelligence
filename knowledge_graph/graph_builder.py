def build_graph(topic, papers, contradictions, gaps):

    html_content = f"""
    <html>
    <head>
    <title>Knowledge Map</title>
    <style>
    body {{
        font-family: Arial;
        padding: 40px;
        background: white;
        color: black;
    }}

    h2 {{
        text-align: center;
    }}

    .paper {{
        margin-bottom: 25px;
    }}

    .gap {{
        margin-left: 20px;
    }}

    .contradiction {{
        margin-left: 20px;
    }}
    </style>
    </head>

    <body>

    <h2>Knowledge Map</h2>

    <h3>Topic: {topic}</h3>
    """

    for i, paper in enumerate(papers[:5]):

        html_content += f"""

        <div class="paper">

        <b>Paper {i+1}:</b> {paper['title']}

        """

        if i < len(gaps):

            html_content += f"""
            <div class="gap">
            Research Gap: {gaps[i]}
            </div>
            """

        if i < len(contradictions):

            html_content += f"""
            <div class="contradiction">
            Contradiction: {contradictions[i]}
            </div>
            """

        html_content += "</div>"

    html_content += """

    </body>
    </html>
    """

    with open("knowledge_graph/graph.html", "w", encoding="utf-8") as f:

        f.write(html_content)

    print("Simple knowledge map generated successfully")