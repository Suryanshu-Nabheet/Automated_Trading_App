import requests

class ZerodhaAPI:
    @staticmethod
    def buy(stock_symbol, amount):
        response = requests.post(
            'https://api.zerodha.com/order',
            json={'symbol': stock_symbol, 'amount': amount, 'action': 'buy'}
        )
        return response.json()
    
    @staticmethod
    def sell(stock_symbol, amount):
        response = requests.post(
            'https://api.zerodha.com/order',
            json={'symbol': stock_symbol, 'amount': amount, 'action': 'sell'}
        )
        return response.json()