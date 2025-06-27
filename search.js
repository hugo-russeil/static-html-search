// When the user types in the search box
document.addEventListener("DOMContentLoaded", function () {
  const input = document.getElementById("searchBox");
  const resultsDiv = document.getElementById("results");

  input.addEventListener("input", function () {
    const term = this.value.trim().toLowerCase();
    resultsDiv.innerHTML = ""; // Clear previous results

    // Skip if search term is too short
    if (term.length < 3) return;

    // Loop through the index
    for (const entry of searchIndex) {
      if (entry.text.toLowerCase().includes(term)) {
        const paragraph = entry.text
          .split(/(?<=[.?!])\s+/)
          .find(p => p.toLowerCase().includes(term)) || entry.text;

        const snippet = paragraph
          .replace(new RegExp(`(${term})`, "gi"), "<mark>$1</mark>")
          .slice(0, 300) + "...";

        const link = document.createElement("a");
        link.href = entry.file;
        link.innerHTML = `
          <strong>${entry.file}</strong><br>
          <small>${snippet}</small><br><br>
        `;

        resultsDiv.appendChild(link);
      }
    }
  });
});
