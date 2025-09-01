# helper_function.py

"""
"""
import yfinance as yf
import matplotlib.pyplot as plt
import os

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# -----------------------------
# Helper: Convert time_frame to start_date
# -----------------------------
def get_start_date_from_df(df, time_frame):
    today = df.index.max()  # last date in the DataFrame
    if time_frame.endswith("y"):
        years = int(time_frame[:-1])
        return today - pd.DateOffset(years=years)
    elif time_frame.endswith("mo"):
        months = int(time_frame[:-2])
        return today - pd.DateOffset(months=months)
    elif time_frame.endswith("d"):
        days = int(time_frame[:-1])
        return today - timedelta(days=days)
    else:
        raise ValueError("Invalid time frame format. Use 'y', 'mo', or 'd'.")

def index_comparison_config():
  # Define the indices and their Yahoo Finance symbols
  indices = {
    "Nifty 50": "^NSEI",
    "Bank Nifty": "^NSEBANK",
    "Nifty IT": "^CNXIT",
    "Nifty Pharma": "^CNXPHARMA",
    "Nifty FMCG": "^CNXFMCG",
    "Nifty Auto": "^CNXAUTO",
    "Nifty Metal": "^CNXMETAL",
    "Nifty Realty": "^CNXREALTY",
    "Nifty Infra": "^CNXINFRA"
  }
  # Choose colors for each index
  colors = {
      "Nifty 50": "black",
      "Bank Nifty": "blue",
      "Nifty IT": "red",
      "Nifty Pharma": "brown",
      "Nifty FMCG": "green",
      "Nifty Auto": "orange",
      "Nifty Metal": "yellow",
      "Nifty Realty": "pink",
      "Nifty Infra": "grey"
  }

  # Choose line width for each index
  linewidths = {
      "Nifty 50": 3.0,  # bold line
      "Bank Nifty": 1.5,
      "Nifty IT": 1.5,
      "Nifty Pharma": 1.5,
      "Nifty FMCG": 1.5,
      "Nifty Auto": 1.5,
      "Nifty Metal": 1.5,
      "Nifty Realty": 1.5,
      "Nifty Infra": 1.5
  }
  # Fetch last 5 years of data
  data = {}
  for name, symbol in indices.items():
      df = yf.download(symbol, period="5y", interval="1d")
      data[name] = df

  return data
  # -----------------------------
  # Slice and Plot
  # -----------------------------
def slice_and_plot(data, time_frame):
    plt.figure(figsize=(14,7))
    for name, df in data.items():
        start_date = get_start_date_from_df(df, time_frame)
        df_slice = df[df.index >= start_date]
        if not df_slice.empty:
            color = colors.get(name, None)
            lw = linewidths.get(name, 1.5)  # default line width 1.5
            plt.plot(df_slice.index, df_slice["Close"] / df_slice["Close"].iloc[0], label=name, color=color, linewidth=lw)

    plt.title(f"NSE Indices Performance ({time_frame})")
    plt.xlabel("Date")
    plt.ylabel("Normalized Close Price")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()

def do_index_comparison():
  data = index_comparison_config()
  slice_and_plot(data, "1mo")
  slice_and_plot(data, "3mo")
  slice_and_plot(data, "6mo")
  slice_and_plot(data, "1y")
