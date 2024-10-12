import React, { useState } from "react";

const Help = ({ message }) => {
  const [showTips, setshowTips] = useState(false);

  return (
    <div
      className="help"
      onMouseEnter={() => setshowTips(true)}
      onMouseLeave={() => setshowTips(false)}
    >
      <img src="/question.png" alt="help" className="icon" />
      {showTips && <div className="tips">{message}</div>}
    </div>
  );
};

export default Help;
