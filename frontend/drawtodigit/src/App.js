import "./App.css";
import React, { useState } from "react";
import Canvas from "./components/Canvas";

function App() {
  const [result, setResult] = useState(null);

  const handlePredict = async (imageData) => {
    try {
      const response = await fetch("http://localhost:500-/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ image: imageData }),
      });
      if (response.ok) {
        const data = await response.json();
        setResult(data.prediction);
      } else {
        console.error("Prediction failed.");
      }
    } catch (error) {
      console.error("Error in fetching prediction: ", error);
    }
  };

  return (
    <div className="App">
      <h1>Draw to Digit</h1>
      <Canvas onPredict={handlePredict} />
      {result !== null && <h2>Predict Digit: {result}</h2>}
    </div>
  );
}

export default App;
