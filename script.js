async function analyze(mode) {
  const asset = document.getElementById("assetInput").value.trim();
  const resultBox = document.getElementById("resultBox");
  const use_ai = mode === "ai";

  if (!asset) {
    resultBox.textContent = "Please enter an asset name.";
    return;
  }

  resultBox.textContent = "Analyzing...";

  try {
    const response = await fetch("https://your-backend-url.onrender.com/get-threat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        asset_name: asset,
        use_ai: use_ai
      })
    });

    const data = await response.json();

    if (use_ai && data.scenario) {
      resultBox.textContent = data.scenario;
    } else if (!use_ai && data.threats && data.threats.length > 0) {
      resultBox.textContent = data.threats.map(t => `
📌 ${t.category}
- Description: ${t.description}
- Impact: ${t.impact}
- Mitigation: ${t.mitigation}
- ISO 21434 Clause: ${t.iso_clause}
      `).join("\n");
    } else {
      resultBox.textContent = "No threats found for this asset.";
    }
  } catch (error) {
    resultBox.textContent = "⚠️ Error reaching backend. Please try again.";
    console.error(error);
  }
}