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

companies = ['11B.WA', 'ABP.WA', 'ACG.WA', 'ACT.WA', 'AGO.WA', 'ALL.WA', 'ALR.WA', 'ALE.WA', 'ALU.WA', 'AMB.WA', 'AMC.WA', 'AMR.WA', 'APT.WA', 'ARC.WA', 'ASB.WA', 'ABS.WA', 'APL.WA', 'ASE.WA', 'AST.WA', 'ATA.WA', 'ATP.WA', 'BFT.WA', 'BXM.WA', 'BML.WA', 'BTN.WA', 'BNP.WA', 'LWB.WA', 'BRS.WA', 'BOS.WA', 'BOW.WA', 'BDX.WA', 'BME.WA', 'CTX.WA', 'CCC.WA', 'CDR.WA', 'CIE.WA', 'CIG.WA', 'CLN.WA', 'COG.WA', 'CMR.WA', 'CMP.WA', 'CPJ.WA', 'CPS.WA', 'DAW.WA', 'DCR.WA', 'DVL.WA', 'DNP.WA', 'DDE.WA', 'ECH.WA', 'ENA.WA', 'ENT.WA', 'ERB.WA', 'ETFB40.WA', 'ETFBND.WA', 'ETFBS8.WA', 'ETFBSX.WA', 'ETFBTB.WA', 'ETFBW2L.WA', 'ETFBW2S.WA', 'ETFBW2T.WA', 'ETFBWT.WA', 'ETFDX.WA', 'ETFSP5.WA', 'EUR.WA', 'FMF.WA', 'FRO.WA', 'FTE.WA', 'GPW.WA', 'GRX.WA', 'GRO.WA', 'ATT.WA', 'GRP.WA', 'BHW.WA', 'HUG.WA', 'ING.WA', 'IKT.WA', 'ICR.WA', 'JSW.WA', 'KER.WA', 'KTY.WA', 'KGH.WA', 'KOG.WA', 'KRU.WA', 'LVC.WA', 'LPP.WA', 'LBA.WA', 'MAB.WA', 'MBK.WA', 'MCI.WA', 'MDG.WA', 'MRT.WA', 'MIL.WA', 'MRB.WA', 'MLS.WA', 'MOB.WA', 'MOL.WA', 'MTL.WA', 'NEU.WA', 'NWG.WA', 'OND.WA', 'OPN.WA', 'OPL.WA', 'PCR.WA', 'PCF.WA', 'PKX.WA', 'PEO.WA', 'PEP.WA', 'PCO.WA', 'PGE.WA', 'PEN.WA', 'PKN.WA', 'PKO.WA', 'PKP.WA', 'PLW.WA', 'PXM.WA', 'PZU.WA', 'R22.WA', 'RBW.WA', 'RWL.WA', 'RVU.WA', 'SNK.WA', 'SPL.WA', 'SCP.WA', 'SEL.WA', 'SLV.WA', 'SHO.WA', 'SKA.WA', 'SPR.WA', 'STX.WA', 'STP.WA', 'STH.WA', 'SNX.WA', 'SGN.WA', 'SNT.WA', 'TPE.WA', 'TIM.WA', 'TOR.WA', 'TOA.WA', 'TEN.WA', 'UNT.WA', 'VRC.WA', 'VGO.WA', 'VOT.WA', 'VOX.WA', 'VRG.WA', 'WWL.WA', 'WLT.WA', 'WPL.WA', 'WTN.WA', 'XTB.WA', 'ZEP.WA']

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
     
def details():
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

    hist = df.history(period="max")

    tab1, tab2 = st.tabs(["Plot", "Raw Data"])

    with tab1:
        plot()

    with tab2:
        st.dataframe(hist)

    with st.expander("📝 Company's details"):
        details()
          
    with st.expander("💰 Financial Data"):
     tab1, tab2, tab3 = st.tabs(["Financials", "Balance Sheet", "Cashflow"])

    with tab1:
        st.header("💵 Financial Statement")
        st.dataframe(df.financials)

    with tab2:
        st.header("⚖️ Balance Sheet")
        st.dataframe(df.balance_sheet)

    with tab3:
        st.header("💸 Cashflow")
        st.dataframe(df.cashflow)

    with st.expander("🎯 Key Performance Indicators"):
     st.header('🎯 Key Performance Indicators')
     kpis = [
        ('🔴 ebitdaMargins:  ',df.info['ebitdaMargins']),
        ('🔴 profitMargins:  ',df.info['profitMargins']),
        ('🔴 operatingCashflow:  ',df.info['operatingCashflow']),
        ('🔴 revenueGrowth:  ',df.info['revenueGrowth']),
        ('🔴 operatingMargins:  ',df.info['operatingMargins']),
        ('🔴 earningsGrowth:  ',df.info['earningsGrowth']),
        ('🔴 currentRatio:  ',df.info['currentRatio']),
        ('🔴 returnOnAssets:  ',df.info['returnOnAssets']),
        ('🔴 debtToEquity:  ',df.info['debtToEquity']),
        ('🔴 returnOnEquity:  ',df.info['returnOnEquity']),
        ('🔴 revenuePerShare:  ',df.info['revenuePerShare']),
        ('🔴 quickRatio:  ',df.info['quickRatio']),
        ('🔴 enterpriseToRevenue:  ',df.info['enterpriseToRevenue']),
        ('🔴 enterpriseToEbitda:  ',df.info['enterpriseToEbitda'])
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
    
