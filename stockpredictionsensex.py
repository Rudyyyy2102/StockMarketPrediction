import yfinance as yf
import pandas as pd
bse30=yf.Ticker("^BSESN")
bse30=bse30.history(period="max")
bse30