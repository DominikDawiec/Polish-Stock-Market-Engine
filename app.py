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
     

     
