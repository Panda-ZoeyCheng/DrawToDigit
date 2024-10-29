import "./App.css";
import React, { useState, useRef } from "react";
import Canvas from "./components/Canvas";
import Help from "./components/Help";

function App() {
  const [result, setResult] = useState("waiting for predict ...");
  const canvasRef = useRef();

  const handlePredict = async (imageData) => {
    setResult(null);

    try {
      const response = await fetch("http://3.27.63.201:5001/predict", {
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
    }
  };

  const resetResult = () => {
    setResult("waiting for predict ...");
  };

  return (
    <div className="outer-container">
      <div className="title">Draw to Digit</div>
      <div className="container">
        <div className="card">
          <Help message="Draw a digit in the canvas, then click 'Predict' to see the result. Use 'Clear' to reset the canvas." />
          <div className="canvas-container">
            <Canvas
              ref={canvasRef}
              onPredict={handlePredict}
              resetResult={resetResult}
            />
            <div className="button-group">
              <button onClick={() => canvasRef.current.handleSubmit()}>
                Predict
              </button>
              <button onClick={() => canvasRef.current.handleClear()}>
                Clear
              </button>
            </div>
          </div>
          <div className="result-container">
            <h2>Result:</h2>
            <p>{result}</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
