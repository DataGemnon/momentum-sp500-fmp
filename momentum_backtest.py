# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 21:27:17 2025

@author: haasm
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# === CONFIG ===
API_KEY = "Xqz3Plda2PdzuAZysmLeR1qL4dsFAcwd"
TICKER = "SPY"  # ETF qui réplique le S&P500
URL = f"https://financialmodelingprep.com/api/v3/historical-price-full/{TICKER}?apikey={API_KEY}"

# === GET DATA ===
def get_data():
    response = requests.get(URL)
    data = response.json()["historical"]
    df = pd.DataFrame(data)
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)
    df = df.sort_index()
    return df[["close"]]

df = get_data()

# === STRATEGY ===
df["SMA50"] = df["close"].rolling(50).mean()
df["SMA200"] = df["close"].rolling(200).mean()

df["Position"] = 0
df.loc[df["SMA50"] > df["SMA200"], "Position"] = 1  # Long when SMA50 > SMA200

df["Returns"] = df["close"].pct_change()
df["Strategy"] = df["Position"].shift(1) * df["Returns"]

# === CUMULATIVE RETURNS ===
df["Cumulative_BuyHold"] = (1 + df["Returns"]).cumprod()
df["Cumulative_Strategy"] = (1 + df["Strategy"]).cumprod()

# === PLOT ===
plt.figure(figsize=(12,6))
plt.plot(df.index, df["Cumulative_BuyHold"], label="Buy & Hold")
plt.plot(df.index, df["Cumulative_Strategy"], label="Momentum Strategy")
plt.legend()
plt.title("Momentum Strategy vs Buy & Hold on S&P500")
plt.show()

# === METRICS ===
sharpe = np.sqrt(252) * df["Strategy"].mean() / df["Strategy"].std()
print("Final Strategy Return:", df["Cumulative_Strategy"].iloc[-1])
print("Final Buy & Hold Return:", df["Cumulative_BuyHold"].iloc[-1])
print("Sharpe Ratio:", sharpe)
