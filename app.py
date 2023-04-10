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

companies = ['11B.WA', 'ABE.WA', 'ACG.WA', 'ACT.WA', 'AGO.WA', 'ALL.WA', 'ALR.WA', 'ALE.WA', 'AML.WA', 'AMB.WA', 'AMC.WA', 'EAT.WA', 'APT.WA', 'ATC.WA', 'ASB.WA', 'ASB.WA', 'ACP.WA', 'ASE.WA', 'ATT.WA', '1AT.WA', 'APR.WA', 'BFT.WA', 'BMX.WA', 'BML.WA', 'BIO.WA', 'BNP.WA', 'LWB.WA', 'BRS.WA', 'BOS.WA', 'BOW.WA', 'BDX.WA', 'BMC.WA', 'TOR.WA', 'CCC.WA', 'CDR.WA', 'CIE.WA', 'CIG.WA', 'CLN.WA', 'COG.WA', 'CMR.WA', 'CMP.WA', 'CRJ.WA', 'CPS.WA', 'DAT.WA', 'DCR.WA', 'DVL.WA', 'DNP.WA', 'DOM.WA', 'ECH.WA', 'ENA.WA', 'ENT.WA', 'ERB.WA', 'EUR.WA', 'FRO.WA', 'FTE.WA', 'GPW.WA', 'GRN.WA', 'GEA.WA', 'GRN.WA', 'ATT.WA', 'GPP.WA', 'BHW.WA', 'HUG.WA', 'ING.WA', 'INK.WA', 'CAR.WA', 'JSW.WA', 'KER.WA', 'KTY.WA', 'KGH.WA', 'KGN.WA', 'KRU.WA', 'LVC.WA', 'LPP.WA', 'LWB.WA', 'MAB.WA', 'MBK.WA', 'MCI.WA', 'MDG.WA', 'MRC.WA', 'MIL.WA', 'MRB.WA', 'MLS.WA', 'MBR.WA', 'MOC.WA', 'MSZ.WA', 'NEU.WA', 'NWG.WA', 'OND.WA', 'OPN.WA', 'OPL.WA', 'PCR.WA', 'PCF.WA', 'PBX.WA', 'PEO.WA', 'PEP.WA', 'PCO.WA', 'PGE.WA', 'PEN.WA', 'PKN.WA', 'PKO.WA', 'PKP.WA', 'PLW.WA', 'PXM.WA', 'PZU.WA', 'R22.WA', 'RBW.WA', 'RWL.WA', 'RVU.WA', 'SNK.WA', 'SPL.WA', 'SCP.WA', 'SEL.WA', 'SLV.WA', 'SHO.WA', 'SNK.WA', 'SPR.WA', 'STX.WA', 'STP.WA', 'STS.WA', 'SNX.WA', 'SGN.WA', 'SNK.WA', 'TPE.WA', 'TIM.WA', 'TOR.WA', 'TOA.WA', 'TSG.WA', 'UNT.WA', 'VRC.WA', 'VGO.WA', 'VOT.WA', 'VOX.WA', 'VRG.WA', 'WWL.WA', 'WLT.WA', 'WPL.WA', 'WTN.WA', 'XTB.WA', 'CCC.WA', 'ETFBM40TR.WA', 'ETFBNDXPL.WA', 'ETFBS80TR.WA', 'ETFBSPXPL.WA', 'ETFBTBSP.WA', 'ETFBW20LV.WA', 'ETFBW20ST.WA', 'ETFBW20TR.WA', 'ETFBWTECH.WA', 'ETFDAX.WA', 'ETFSP500.WA']

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
     df['EMA_9'] = df['Close'].ewm(9).mean().shift()
     df['EMA_22'] = df['Close'].ewm(22).mean().shift()
     df['SMA_5'] = df['Close'].rolling(5).mean().shift()
     df['SMA_10'] = df['Close'].rolling(10).mean().shift()
     df['SMA_15'] = df['Close'].rolling(15).mean().shift()
     df['SMA_30'] = df['Close'].rolling(30).mean().shift()
     df['RSI'] = RSI(df).fillna(0)
     EMA_12 = pd.Series(df['Close'].ewm(span=12, min_periods=12).mean())
     EMA_26 = pd.Series(df['Close'].ewm(span=26, min_periods=26).mean())
     df['MACD'] = pd.Series(EMA_12 - EMA_26)
     df['MACD_signal'] = pd.Series(df.MACD.ewm(span=9, min_periods=9).mean())

     indicators = [
         ('EMA 9', 'EMA_9'),
         ('EMA 22', 'EMA_22'),
         ('SMA 5', 'SMA_5'),
         ('SMA 10', 'SMA_10'),
         ('SMA 15', 'SMA_15'),
         ('SMA 30', 'SMA_30'),
     ]

     fig = go.Figure()
     for name, column in indicators:
         fig.add_trace(go.Scatter(x=df.index, y=df[column], name=name))
     fig.add_trace(go.Scatter(x=df.index, y=df.Close, name='Close', opacity=0.3))
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
      
    with st.expander("📊 Buy/Sell Signals"):
     st.header('📊 Buy/Sell Signals')

     df = hist
     
     df["SMA50"] = df["Close"].rolling(window=50).mean()
     df["SMA200"] = df["Close"].rolling(window=200).mean()

     df["Signal"] = 0
     df.loc[df["SMA50"] > df["SMA200"], "Signal"] = 1
     df["Position"] = df["Signal"].diff()
     buy_signals = df[df["Position"] == 1]
     sell_signals = df[df["Position"] == -1]
     
     current_signal = df["Signal"].tail(1).values[0]
     if current_signal == 1:
         st.header("Current signal: Buy")
     else:
         st.header("Current signal: Sell")

     # Create a figure with one subplot
     fig = go.Figure()

     # Plot the stock price and moving averages
     fig.add_trace(go.Scatter(x=df.index, y=df["Close"], name="Price"))
     fig.add_trace(go.Scatter(x=df.index, y=df["SMA50"], name="50-day SMA"))
     fig.add_trace(go.Scatter(x=df.index, y=df["SMA200"], name="200-day SMA"))

     # Plot the buy and sell signals
     fig.add_trace(go.Scatter(x=buy_signals.index, y=df.loc[buy_signals.index, "Close"], mode="markers", marker=dict(symbol="triangle-up", size=10, color="green"), name="Buy"))
     fig.add_trace(go.Scatter(x=sell_signals.index, y=df.loc[sell_signals.index, "Close"], mode="markers", marker=dict(symbol="triangle-down", size=10, color="red"), name="Sell"))

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
