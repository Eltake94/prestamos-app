import requests
import time

symbols = [
    "BTCUSDT",
    "ETHUSDT",
    "SOLUSDT",
    "XRPUSDT",
    "DOGEUSDT",
    "TRXUSDT",
    "ADAUSDT",
    "AVAXUSDT"
]

def binance(s):
    return float(requests.get("https://api.binance.com/api/v3/ticker/price?symbol="+s).json()["price"])

def bybit(s):
    return float(requests.get("https://api.bybit.com/v5/market/tickers?category=spot&symbol="+s).json()["result"]["list"][0]["lastPrice"])

while True:
    print("\n---")
    for s in symbols:
        try:
            b = binance(s)
            y = bybit(s)
            print(s, "Binance:", b, "Bybit:", y)
        except:
            print("error en", s)
    time.sleep(5)
