document.getElementById("predictForm").addEventListener("submit", function(e) {
  e.preventDefault();

  const data = {
    medinc: parseFloat(document.getElementById("medinc").value),
    averooms: parseFloat(document.getElementById("averooms").value),
    aveoccup: parseFloat(document.getElementById("aveoccup").value)
    // Add more fields here if needed
  };

  fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  })
  .then(res => res.json())
  .then(result => {
    document.getElementById("result").innerText = `Predicted Price: ₹${result.prediction.toFixed(2)}`;
  })
  .catch(err => {
    document.getElementById("result").innerText = "Error: Unable to get prediction";
    console.error(err);
  });
});
