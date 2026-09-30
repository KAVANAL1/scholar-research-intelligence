import os
from html import escape


def build_knowledge_graph(topic, papers, gaps, contradictions):
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Knowledge Map - {escape(str(topic))}</title>
<style>
    * {{
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }}
    body {{
        background: #f8fafc;
        color: #0f172a;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        padding: 24px;
        line-height: 1.6;
    }}
    .header {{
        margin-bottom: 24px;
        padding-bottom: 16px;
        border-bottom: 1px solid #e2e8f0;
    }}
    .header h2 {{
        font-size: 20px;
        color: #0f172a;
        font-weight: 600;
        display: flex;
        align-items: center;
        gap: 8px;
    }}
    .header .topic-tag {{
        display: inline-block;
        font-size: 13px;
        color: #2563eb;
        background: #eff6ff;
        padding: 3px 10px;
        border-radius: 9999px;
        font-weight: 500;
        margin-top: 6px;
    }}
    .paper-block {{
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 18px 20px;
        margin-bottom: 16px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
        transition: box-shadow 0.2s ease;
    }}
    .paper-block:hover {{
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.08);
    }}
    .paper-title {{
        font-weight: 600;
        font-size: 16px;
        color: #1e293b;
        margin-bottom: 12px;
        display: flex;
        align-items: baseline;
        gap: 8px;
    }}
    .paper-index {{
        background: #e2e8f0;
        color: #475569;
        font-size: 11px;
        font-weight: 700;
        padding: 2px 7px;
        border-radius: 6px;
        text-transform: uppercase;
    }}
    .meta-box {{
        display: grid;
        grid-template-columns: 1fr;
        gap: 10px;
        margin-top: 10px;
    }}
    .item-row {{
        background: #f8fafc;
        border-radius: 8px;
        padding: 10px 14px;
        font-size: 13px;
        border-left: 3px solid #cbd5e1;
    }}
    .item-row.gap {{
        border-left-color: #f59e0b;
        background: #fffbeb;
        color: #92400e;
    }}
    .item-row.contradiction {{
        border-left-color: #6366f1;
        background: #eef2ff;
        color: #3730a3;
    }}
    .label {{
        font-weight: 600;
        margin-bottom: 2px;
        display: flex;
        align-items: center;
        gap: 6px;
    }}
</style>
</head>
<body>

<div class="header">
    <h2>Knowledge Intelligence Map</h2>
    <span class="topic-tag">Topic: {escape(str(topic))}</span>
</div>
"""

    for i, paper in enumerate(papers):
        gap = gaps[i] if i < len(gaps) else "No gap detected"
        contradiction = (
            contradictions[i] if i < len(contradictions)
            else "No contradiction detected"
        )

        title = escape(str(paper.get("title", f"Paper {i+1}")))
        gap = escape(str(gap))
        contradiction = escape(str(contradiction))

        html_content += f"""
    <div class="paper-block">
        <div class="paper-title">
            <span class="paper-index">Paper {i+1}</span>
            <span>{title}</span>
        </div>
        <div class="meta-box">
            <div class="item-row gap">
                <div class="label">🔬 Identified Research Gap</div>
                <div>{gap}</div>
            </div>
            <div class="item-row contradiction">
                <div class="label">⚖️ Comparative Analysis / Contradiction</div>
                <div>{contradiction}</div>
            </div>
        </div>
    </div>
"""

    html_content += "</body>\n</html>"

    os.makedirs("knowledge_graph", exist_ok=True)

    with open("knowledge_graph/graph.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    return "knowledge_graph/graph.html"


def build_graph(papers, analysis):
    """Compatibility alias for tests."""
    gaps = []
    contradictions = []
    return build_knowledge_graph("Research Analysis", papers, gaps, contradictions)
