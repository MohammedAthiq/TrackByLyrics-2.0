function toggleTheme() {
    document.body.classList.toggle("dark");
}

async function searchSong() {
    const query = document.getElementById("lyricsInput").value.trim();
    const resultDiv = document.getElementById("result");

    if (!query) {
        resultDiv.innerHTML = "<p>Please enter some lyrics or a song name.</p>";
        return;
    }

    resultDiv.innerHTML = "<p>🔎 Searching...</p>";

    try {
        const response = await fetch("/api/search", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ lyrics: query })
        });

        const data = await response.json();

        if (data.error) {
            resultDiv.innerHTML = `<p>${data.error}</p>`;
        } else {
            resultDiv.innerHTML = `
                <div class="song-card">
                    <h2>${data.name}</h2>
                    <p><strong>Artist:</strong> ${data.artist}</p>
                    ${data.image ? `<img src="${data.image}" alt="Album Art">` : ""}
                    <a href="${data.url}" class="spotify-link" target="_blank">🎧 Listen on Spotify</a>
                    ${data.preview ? `
                        <div class="preview">
                            <p>🎵 Preview:</p>
                            <audio controls>
                                <source src="${data.preview}" type="audio/mpeg">
                                Your browser does not support the audio element.
                            </audio>
                        </div>` : ""}
                </div>
            `;
        }
    } catch (error) {
        resultDiv.innerHTML = "<p>⚠️ Something went wrong. Please try again later.</p>";
    }
}