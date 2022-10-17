import pandas as pd
import numpy as np

import streamlit as st
     
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go
import plotly.io as pio
pio.templates.default = "plotly"

from datetime import date

import matplotlib.pyplot as plt
import warnings

import xlsxwriter
import io

# import warnings
warnings.filterwarnings('ignore')

import yfinance as yf











companies = ('MSFT','GOOG')

option = st.selectbox('Choose company', companies)

if option:
     df =  yf.Ticker(option)
     st.write(df.info)
     
     hist = df.history(period="max")
     
     fig = go.Figure([go.Scatter(x=hist.index, y=hist['Close'])])

     fig.update_xaxes(rangeslider_visible=True, rangeselector=dict(
         buttons=list([
                 dict(count=1, label="1m", step="month", stepmode="backward"),
                 dict(count=6, label="6m", step="month", stepmode="backward"),
                 dict(count=1, label="YTD", step="year", stepmode="todate"),
                 dict(count=1, label="1y", step="year", stepmode="backward"),
                 dict(step="all")
             ])
         )
     )

     st.plotly_chart(fig)
     
     
     
     fig = go.Figure()
     fig.add_trace(go.Scatter(x=hist.index, y=hist['Volume']))
     st.plotly_chart(fig)
     
     
     
     #EMA
     df['EMA_9'] = df['Close'].ewm(9).mean().shift()
     df['EMA_22'] = df['Close'].ewm(22).mean().shift()
     #SMA
     df['SMA_5'] = df['Close'].rolling(5).mean().shift()
     df['SMA_10'] = df['Close'].rolling(10).mean().shift()
     df['SMA_15'] = df['Close'].rolling(15).mean().shift()
     df['SMA_30'] = df['Close'].rolling(30).mean().shift()
     #RSI14
     def RSI(df, n=14):
         close = df['Close']
         delta = close.diff()
         delta = delta[1:]
         pricesUp = delta.copy()
         pricesDown = delta.copy()
         pricesUp[pricesUp < 0] = 0
         pricesDown[pricesDown > 0] = 0
         rollUp = pricesUp.rolling(n).mean()
         rollDown = pricesDown.abs().rolling(n).mean()
         rs = rollUp / rollDown
         rsi = 100.0 - (100.0 / (1.0 + rs))
         return rsi

     df['RSI'] = RSI(df).fillna(0)

     EMA_12 = pd.Series(df['Close'].ewm(span=12, min_periods=12).mean())
     EMA_26 = pd.Series(df['Close'].ewm(span=26, min_periods=26).mean())
     df['MACD'] = pd.Series(EMA_12 - EMA_26)
     df['MACD_signal'] = pd.Series(df.MACD.ewm(span=9, min_periods=9).mean())
     
#####################################

     fig = go.Figure()
     fig.add_trace(go.Scatter(x=df.index, y=df.EMA_9, name='EMA 9'))
     fig.add_trace(go.Scatter(x=df.index, y=df.EMA_22, name='EMA 22'))
     fig.add_trace(go.Scatter(x=df.index, y=df.SMA_5, name='SMA 5'))
     fig.add_trace(go.Scatter(x=df.index, y=df.SMA_10, name='SMA 10'))
     fig.add_trace(go.Scatter(x=df.index, y=df.SMA_15, name='SMA 15'))
     fig.add_trace(go.Scatter(x=df.index, y=df.SMA_30, name='SMA 30'))
     fig.add_trace(go.Scatter(x=df.index, y=df.Close, name='Close', opacity=0.3))
     st.plotly_chart(fig)
     
##############################################

     fig = go.Figure(go.Scatter(x=df.index, y=df.RSI, name='RSI'))
     st.plotly_chart(fig)
