async function search() {

    let query = document.getElementById("query").value;

    const response = await fetch(

        `http://127.0.0.1:8000/research?topic=${query}`

    );

    const data = await response.json();

    let output = "";


 output += "<h3>📄 Top Papers</h3>";

if (data.papers && data.papers.length > 0) {

    data.papers.forEach(p => {

        output += `
        <p>
        <b>${p.title}</b><br>

        📊 Citations: ${p.citations}<br>

        🔗 <a href="${p.url}" target="_blank">Open Paper</a>

        ${p.pdf ? ` | 📄 <a href="${p.pdf}" target="_blank">Download PDF</a>` : ""}

        </p>
        `;

    });

}


    output += "<h3>Research Gaps</h3>";

    data.gaps.forEach(g => {

        output += `<p>• ${g}</p>`;

    });


    output += "<h3>Contradictions</h3>";

    data.contradictions.forEach(c => {

        output += `<p>• ${c}</p>`;

    });


    output += "<h3>Literature Review</h3>";

    output += `<pre>${data.review}</pre>`;


    document.getElementById("results").innerHTML = output;

}