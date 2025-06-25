async function analyze() {
  const asset = document.getElementById("assetInput").value;
  const resultBox = document.getElementById("resultBox");

  try {
    const response = await fetch("https://your-api-url.onrender.com/get-threat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ asset_name: asset })
    });

    const data = await response.json();

    if (data.threats.length > 0) {
      resultBox.textContent = JSON.stringify(data.threats, null, 2);
    } else {
      resultBox.textContent = "No threats found for this asset.";
    }
  } catch (error) {
    resultBox.textContent = "Error: Unable to reach the backend.";
  }
}
