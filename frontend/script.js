function search() {

    let query = document.getElementById("query").value;

    if (!query) {

        alert("Enter topic");

        return;

    }

    document.getElementById("results").innerHTML = `

    <div class="loader"></div>

    `;


    fetch(`http://127.0.0.1:8000/research?topic=${query}`)

    .then(res => res.json())

    .then(data => {

        display(data);

    })

}



function display(data) {

    let output = "";


    // PAPERS

    output += `<div class="card">

    <h2>📄 Top Papers</h2>`;



    data.papers.forEach(p => {

        output += `

        <p>

        <b>${p.title}</b>

        <br>

        📊 Citations: ${p.citations}

        <br>

        <a href="${p.url}" target="_blank">🔗 Open Paper</a>

        ${p.pdf ? `<a href="${p.pdf}" target="_blank"> | 📄 PDF</a>` : ""}

        </p>

        `;

    });



    output += "</div>";



    // GAPS

    output += `<div class="card">

    <h2>🧪 Research Gaps</h2>`;



    data.gaps.forEach(g => {

        output += `<p>• ${g}</p>`;

    });



    output += "</div>";



    // CONTRADICTIONS

    output += `<div class="card">

    <h2>⚖️ Contradictions</h2>`;



    data.contradictions.forEach(c => {

        output += `<p>• ${c}</p>`;

    });



    output += "</div>";



    // REVIEW

    output += `

    <div class="card">

    <h2>📚 Literature Review</h2>

    <pre>${data.review}</pre>

    </div>

    `;



    // GRAPH

   output += `

<div class="card">

<h2>📊 Knowledge Graph</h2>

<iframe

src="../knowledge_graph/graph.html"

width="100%"

height="600px"

style="border:none; border-radius:15px;">

</iframe>

</div>

`; 



    document.getElementById("results").innerHTML = output;

}