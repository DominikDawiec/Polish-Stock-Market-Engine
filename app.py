# importing required packages 
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
import plotly.io as pio
import matplotlib.pyplot as plt
import xlsxwriter
import io
import yfinance as yf

# set page configuration
st.set_page_config(layout="centered", page_icon="📈", page_title="Polish Stock Market App")

# display title
st.title("📈 Polish Stock App")

companies = ['11B.WA', 'ACG.WA', 'AGO.WA', 'ALL.WA', 'ALR.WA', 'ALE.WA']

with st.sidebar:
     option = st.selectbox('Please select company', companies)

def plot():
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=hist.index,
        y=hist['Open'],
        mode='lines',
        name='Open',
        line_color='rgb(5, 177, 59)'
    ))

    fig.add_trace(go.Scatter(
        x=hist.index,
        y=hist['Low'],
        mode='lines',
        name='Low',
        line_color='rgb(50, 30, 197)'
    ))

    fig.add_trace(go.Scatter(
        x=hist.index,
        y=hist['High'],
        mode='lines',
        name='High',
        line_color='rgb(243, 187, 112)'
    ))

    fig.add_trace(go.Scatter(
        x=hist.index,
        y=hist['Close'],
        mode='lines',
        name='Close',
        line_color='rgb(193, 8, 0)'
    ))

    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
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
     
def details(): #Most on the variables below are no longer supported by yfinance (April 2023)
    st.header("📝 Company's details")

    details = [
        ("Full name: ", df.info['longName']),
        ("Sector: ", df.info['sector']), 
        ("Industry: ", df.info['industry']), 
        ("Country: ", df.info['country']),
        ("City: ", df.info['city']),
        ("Address: ", df.info['address1']),
        ("Zip: ", df.info['zip']),
        ("Summary: ", df.info['longBusinessSummary']),
        ("Website: ", df.info['website'])
    ]

    for name, value in details:
        st.write(name, value)

if option:
    df = yf.Ticker(option)

    name = df.info['longName']
    st.header(name)

    hist = df.history(period="max")

    tab1, tab2 = st.tabs(["Plot", "Raw Data"])

    with tab1:
        plot()

    with tab2:
        st.dataframe(hist)

    with st.expander("🎯 Key Performance Indicators"):
     st.header('🎯 Key Performance Indicators')
     kpis = [
        ('🔴 Market capitalization:  ',df.info['marketCap']),
        ('🔴 Dividend yield:  ',df.info['trailingAnnualDividendYield']),
        ('🔴 Price-to-earnings ratio (P/E):  ',df.info['trailingPE']),
        ('🔴 Average analyst rating:  ',df.info['averageAnalystRating']),
        ('🔴 Fifty-two week high/low:  ',df.info['fiftyTwoWeekRange'])
    ]
     for name, value in kpis:
          st.write(name, value)
     
    with st.expander("📊 Technical Analysis"):
     st.header('📊 Technical Analysis')
     #EMA
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

     df = hist
     df['SMA50'] = df['Close'].rolling(50).mean().shift()
     df['SMA200'] = df['Close'].rolling(200).mean().shift(

     fig = go.Figure()
     
     fig.add_trace(go.Scatter(x=hist.index, y=hist["Close"], name="Price"))
     fig.add_trace(go.Scatter(x=hist.index, y=hist["SMA50"], name="50-day SMA"))
     fig.add_trace(go.Scatter(x=hist.index, y=hist["SMA200"], name="200-day SMA"))
          

          
     fig.update_xaxes(rangeslider_visible=True, rangeselector=dict(
         buttons=list([
             dict(count=1, label="1m", step="month", stepmode="backward"),
             dict(count=6, label="6m", step="month", stepmode="backward"),
             dict(count=1, label="YTD", step="year", stepmode="todate"),
             dict(count=1, label="1y", step="year", stepmode="backward"),
             dict(step="all")
         ])
     ))
     st.plotly_chart(fig)
    
