import React from "react";

const Result = ({ result }) => {
  return (
    <div>
      <h2>Predction Result:</h2>
      {result !== null ? (
        <p>
          The predicted digit is: <strong>{result}</strong>
        </p>
      ) : (
        <p>No prediction yet. Please draw a digit and click "Predict".</p>
      )}
    </div>
  );
};

export default Result;
