let researchData = null;


/* =========================
   SEARCH
========================= */

function search() {

    const query = document.getElementById("query").value.trim();

    if (!query) {
        alert("Please enter a research topic.");
        return;
    }

    const results = document.getElementById("results");
    const emptyState = document.getElementById("empty-state");
    const status = document.getElementById("search-status");

    emptyState.classList.add("hidden");
    results.classList.remove("hidden");

    status.innerHTML = `
        <div class="loading">
            <div class="spinner"></div>
            <span>Searching papers and analyzing research...</span>
        </div>
    `;

    document.getElementById("papers-content").innerHTML = "";
    document.getElementById("gaps-content").innerHTML = "";
    document.getElementById("contradictions-content").innerHTML = "";
    document.getElementById("review-content").innerHTML = "";

    fetch(
        `/research?topic=${encodeURIComponent(query)}`
    )

    .then(response => {

        if (!response.ok) {
            throw new Error("Backend returned an error.");
        }

        return response.json();
    })

    .then(data => {

        researchData = data;

        status.innerHTML =
            `Research completed for <strong>${escapeHTML(data.topic)}</strong>`;

        displayPapers(data);

        displayGaps(data);

        displayContradictions(data);

        displayReview(data);

        // Load knowledge graph
        document.getElementById("knowledge-graph").src =
            "/graph/graph.html?t=" + Date.now();

    })

    .catch(error => {

        console.error(error);

        status.innerHTML = `
            <span style="color:#dc2626">
                Unable to complete the research request.
                ${escapeHTML(error.message)}
            </span>
        `;

    });
}


/* =========================
   PAPERS
========================= */

function displayPapers(data) {

    const container =
        document.getElementById("papers-content");

    document.getElementById("paper-count").textContent =
        `${data.papers.length} papers`;

    if (!data.papers.length) {

        container.innerHTML =
            `<div class="analysis-card">
                No papers were found for this topic.
            </div>`;

        return;
    }

    let html = "";

    data.papers.forEach((paper, index) => {

        html += `

        <div class="paper-card">

            <div class="paper-title">
                ${escapeHTML(paper.title)}
            </div>

            <div class="paper-meta">

                <span>
                    <svg class="ic" viewBox="0 0 24 24"><use href="#i-chart-line"/></svg>
                    ${paper.citations || 0} citations
                </span>

                <span>
                    Paper ${index + 1}
                </span>

            </div>

            <div class="paper-links">

                ${
                    paper.url
                    ?
                    `<a href="${safeUrl(paper.url)}" target="_blank" rel="noopener">
                        <svg class="ic" viewBox="0 0 24 24"><use href="#i-arrow-up-right-from-square"/></svg>
                        Open source
                    </a>`
                    :
                    ""
                }

                ${
                    paper.pdf
                    ?
                    `<a href="${safeUrl(paper.pdf)}" target="_blank" rel="noopener">
                        <svg class="ic" viewBox="0 0 24 24"><use href="#i-file-lines"/></svg>
                        PDF
                    </a>`
                    :
                    ""
                }

            </div>

        </div>

        `;

    });

    container.innerHTML = html;
}


/* =========================
   RESEARCH GAPS
========================= */

function displayGaps(data) {

    const container =
        document.getElementById("gaps-content");

    data.gaps = toList(data.gaps);

    if (data.gaps.length === 0) {

        container.innerHTML =
            `<div class="analysis-card">
                No research gaps were identified.
            </div>`;

        return;
    }

    let html = "";

    data.gaps.forEach((gap, index) => {

        html += `

        <div class="analysis-card">

            <span class="analysis-number">
                ${index + 1}
            </span>

            ${renderInline(gap)}

        </div>

        `;

    });

    container.innerHTML = html;
}


/* =========================
   CONTRADICTIONS
========================= */

function displayContradictions(data) {

    const container =
        document.getElementById("contradictions-content");

    data.contradictions = toList(data.contradictions);

    if (data.contradictions.length === 0) {

        container.innerHTML =
            `<div class="analysis-card">
                No major contradictions were identified.
            </div>`;

        return;
    }

    let html = "";

    data.contradictions.forEach((item, index) => {

        html += `

        <div class="analysis-card">

            <span class="analysis-number">
                ${index + 1}
            </span>

            ${renderInline(item)}

        </div>

        `;

    });

    container.innerHTML = html;
}


/* =========================
   LITERATURE REVIEW
========================= */

function displayReview(data) {

    const container =
        document.getElementById("review-content");

    container.innerHTML = renderMarkdown(data.review || "No literature review generated.");
}


/* =========================
   SIDEBAR NAVIGATION
========================= */

document.querySelectorAll(".nav-item").forEach(button => {

    button.addEventListener("click", () => {

        const section =
            button.getAttribute("data-section");

        document.querySelectorAll(".nav-item")
            .forEach(item => item.classList.remove("active"));

        button.classList.add("active");

        document.querySelectorAll(".content-section")
            .forEach(item => item.classList.remove("active-section"));

        const target =
            document.getElementById(section);

        if (target) {
            target.classList.add("active-section");
        }

    });

});


/* =========================
   TEXT FORMATTING
========================= */

function formatText(text) {

    if (!text) {
        return "";
    }

    let safe = escapeHTML(text);

    // Make **important text** bold
    safe = safe.replace(
        /\*\*(.*?)\*\*/g,
        "<strong>$1</strong>"
    );

    return safe;
}


/* =========================
   HTML ESCAPE
========================= */

function escapeHTML(text) {

    if (text === null || text === undefined) {
        return "";
    }

    return String(text)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}

/* =========================
   HELPERS (markdown, lists, urls)
========================= */

function renderMarkdown(text) {
    if (typeof marked === 'undefined' || typeof DOMPurify === 'undefined') return '<pre>' + escapeHTML(text) + '</pre>';
    return DOMPurify.sanitize(marked.parse(String(text)));
}

function renderInline(text) {
    if (typeof marked === 'undefined' || typeof DOMPurify === 'undefined') return escapeHTML(text);
    return DOMPurify.sanitize(marked.parseInline(String(text)));
}

// Accepts an array, or one string with "-", "*", "•" or "1." bullets
function toList(value) {
    if (Array.isArray(value)) return value.filter(Boolean);
    if (!value) return [];
    return String(value)
        .split(/\n+/)
        .map(l => l.replace(/^\s*(?:[-*\u2022]|\d+[.)])\s+/, "").trim())
        .filter(Boolean);
}

function safeUrl(url) {
    return /^https?:\/\//i.test(url) ? escapeHTML(url) : "#";
}

