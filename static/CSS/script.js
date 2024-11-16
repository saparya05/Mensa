const quotesContainer = document.querySelector("#para");
const authorContainer = document.querySelector("#author");

async function fetchQuote() {
    try {
        quotesContainer.textContent = "Loading...";
        authorContainer.textContent = "";

        const response = await fetch("https://type.fit/api/quotes");
        if (!response.ok) throw new Error("Failed to fetch");

        const data = await response.json();
        const quote = data[0].q;
        const author = data[0].a;

        quotesContainer.textContent = `"${quote}"`;
        authorContainer.textContent = `- ${author}`;
    } catch (error) {
        console.error("Error fetching quote:", error);
        quotesContainer.textContent = "Failed to fetch quotes. Try again later.";
        authorContainer.textContent = "";
    }
}

function startSlideshow() {
    fetchQuote(); // Fetch an initial quote
    setInterval(fetchQuote, 5000); // Fetch a new quote every 5 seconds
}

startSlideshow();
