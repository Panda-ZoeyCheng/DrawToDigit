import "./App.css";
import React, { useState } from "react";
import Canvas from "./components/Canvas";
import Result from "./components/Result";

function App() {
  const [result, setResult] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handlePredict = async (imageData) => {
    setIsLoading(true);
    setResult(null);

    try {
      const response = await fetch("http://localhost:5001/predict", {
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
        const errorData = await response.json();
        console.error("Prediction failed: ", errorData);
        setResult("Prediction failed");
      }
    } catch (error) {
      console.error("Error in fetching prediction: ", error);
      setResult("Error occurred");
    } finally {
      setIsLoading(false);
    }
  };

  const resetResult = () => {
    setResult(null);
  };

  return (
    <div className="App">
      <h1>Draw to Digit</h1>
      <Canvas onPredict={handlePredict} resetResult={resetResult} />
      {isLoading ? <p>Predicting...</p> : <Result result={result} />}
    </div>
  );
}

export default App;
