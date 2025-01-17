import React, { useState, useEffect } from "react";

const App = () => {
  const [stockSymbol, setStockSymbol] = useState("");
  const [action, setAction] = useState("");
  const [amount, setAmount] = useState(0);
  const [prediction, setPrediction] = useState(null);

  useEffect(() => {
    const fetchPrediction = async () => {
      const response = await fetch(`/api/predict_trade?symbol=${stockSymbol}`);
      const data = await response.json();
      setPrediction(data.prediction);
    };

    if (stockSymbol) {
      fetchPrediction();
    }
  }, [stockSymbol]);

  const handleTrade = async () => {
    const response = await fetch("/execute_trade", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ symbol: stockSymbol, action, amount }),
    });

    const result = await response.json();
    alert(result.status);
  };

  return (
    <div className="App">
      <h1>AI-Powered Automated Trading</h1>
      <div>
        <input
          type="text"
          value={stockSymbol}
          onChange={(e) => setStockSymbol(e.target.value)}
          placeholder="Enter stock symbol"
        />
        <button onClick={handleTrade}>Execute Trade</button>
      </div>
      <div>
        <label>Action:</label>
        <select onChange={(e) => setAction(e.target.value)}>
          <option value="buy">Buy</option>
          <option value="sell">Sell</option>
        </select>
      </div>
      <div>
        <label>Amount:</label>
        <input
          type="number"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
        />
      </div>
    </div>
  );
};

export default App;