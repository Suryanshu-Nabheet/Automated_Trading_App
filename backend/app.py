from flask import Flask, request, jsonify
import requests
import json
from zerodha_api import ZerodhaAPI

app = Flask(__name__)

@app.route('/execute_trade', methods=['POST'])
def execute_trade():
    data = request.json
    stock_symbol = data.get('symbol')
    action = data.get('action')
    amount = data.get('amount')

    prediction = predict_trade(stock_symbol)

    if prediction == 'buy' and action == 'buy':
        result = ZerodhaAPI.buy(stock_symbol, amount)
    elif prediction == 'sell' and action == 'sell':
        result = ZerodhaAPI.sell(stock_symbol, amount)
    else:
        result = {'status': 'no action'}

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)