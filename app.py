# importing all required packages 

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

###############################################################

st.set_page_config(layout="centered", page_icon="📈", page_title="Polish Stock Market App")

###############################################################

st.title("📈 Polish Stock App")

#####################################################

companies = ('ALE.WA', 'PLW.WA', 'ANR.WA', 'CMP.WA', 'KGH.WA', 'MEX.WA')

####################################################

with st.sidebar:
     option = st.selectbox('Please select company', companies)

###############################################################


def plot():
     fig = go.Figure([go.Scatter(x=hist.index, y=hist['Open'], 
                    mode='lines', 
                    name='Open', 
                    line_color='rgb(0,100,80)'
                    )])
     
     fig.add_trace(go.Scatter(x=hist.index, y=hist['Low'],
                    mode='lines',
                    name='Low',
                    line_color='rgb(0,100,80)'
                    ))
     fig.add_trace(go.Scatter(x=hist.index, y=hist['High'],
                    mode='lines',
                    name='High',
                    line_color='rgb(0,100,80)'
                    ))
     fig.add_trace(go.Scatter(x=hist.index, y=hist['Close'],
                    mode='lines',
                    name='Close',
                    line_color='rgb(0,100,80)'
                    ))

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
     
#######################################################################################3

def details():
     
     st.header("📝 Company's details")
     
     st.write('Full name: ', str(df.info['longName']))
     st.write('Sector: ', str(df.info['sector']))
     st.write('Industry: ', str(df.info['industry']))
     st.write('Country: ', str(df.info['country']))
     st.write('City: ', str(df.info['city']))
     st.write('Address: ', str(df.info['address1']))
     st.write('Zip: ', str(df.info['zip']))
     st.write('Summary: ', str(df.info['longBusinessSummary']))
     st.write('Website: ', str(df.info['website']))
     
###############################################################

if option:
     
     df =  yf.Ticker(option)
     
     # Setting the header
     st.header(df.info['longName'])
     
     # def get data
     hist = df.history(period="max")
     
     ######################################################################
     
     tab1, tab2 = st.tabs(["Plot", "Raw Data"])
     
     with tab1:
          plot()
               
     with tab2:          
          st.dataframe(hist)
     
     ###################################################################### 
     
     with st.expander("📝 Company's details"):
                    
          details()

          
     ##########################################################
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
     
     ######################################
     with st.expander("🎯 Key Performance Indicators"):
          tab1, tab2 = st.tabs(["KPI", "KPI with wytlumaczenie"])
          
          with tab1:
               st.header('🎯 Key Performance Indicators')
               st.write('🔴 ebitdaMargins:  ',df.info['ebitdaMargins'])
               st.write('🔴 profitMargins:  ',df.info['profitMargins'])
               st.write('🔴 operatingCashflow:  ',df.info['operatingCashflow'])
               st.write('🔴 revenueGrowth:  ',df.info['revenueGrowth'])
               st.write('🔴 operatingMargins:  ',df.info['operatingMargins'])
               st.write('🔴 earningsGrowth:  ',df.info['earningsGrowth'])
               st.write('🔴 currentRatio:  ',df.info['currentRatio'])
               st.write('🔴 returnOnAssets:  ',df.info['returnOnAssets'])
               st.write('🔴 debtToEquity:  ',df.info['debtToEquity'])
               st.write('🔴 returnOnEquity:  ',df.info['returnOnEquity'])
               st.write('🔴 revenuePerShare:  ',df.info['revenuePerShare'])
               st.write('🔴 quickRatio:  ',df.info['quickRatio'])
               st.write('🔴 enterpriseToRevenue:  ',df.info['enterpriseToRevenue'])
               st.write('🔴 enterpriseToEbitda:  ',df.info['enterpriseToEbitda'])
               
          with tab2:
               st.header('🔴 Key Performance Indicators')
               st.write("🔴 ebitdaMargins:  measure of a company's operating profit as a percentage of its revenue",df.info['ebitdaMargins'])
               st.write('🔴 profitMargins:  measure of profitability',df.info['profitMargins'])
               st.write('🔴 operatingCashflow:  measure of the amount of cash generated by a company's normal business operations',df.info['operatingCashflow'])
               st.write("🔴 revenueGrowth:  the increase (or decrease) in a company's sales from one period to the next",df.info['revenueGrowth'])
               st.write('🔴 operatingMargins:  measures how much profit a company makes on a dollar of sales after paying for variable costs of production',df.info['operatingMargins'])
               st.write("🔴 earningsGrowth:  measure of the increase in a company's income in a particular period",df.info['earningsGrowth'])
               st.write('🔴 currentRatio:   liquidity ratio that measures whether a firm has enough resources to meet its short-term obligations',df.info['currentRatio'])
               st.write('🔴 returnOnAssets:  financial ratio that indicates how profitable a company is in relation to its total assets',df.info['returnOnAssets'])
               st.write("🔴 debtToEquity:  measures your company's total debt relative to the amount originally invested by the owners and the earnings that have been retained over time",df.info['debtToEquity'])
               st.write("🔴 returnOnEquity:  measure of financial performance calculated by dividing net income by shareholders' equity",df.info['returnOnEquity'])
               st.write("🔴 revenuePerShare:  ratio that computes the total revenue earned per share over a designated period, whether quarterly, semi-annually, annually, or trailing twelve months (TTM) ",df.info['revenuePerShare'])
               st.write("🔴 quickRatio:  measures a company's capacity to pay its current liabilities without needing to sell its inventory or obtain additional financing",df.info['quickRatio'])
               st.write('🔴 enterpriseToRevenue:  for any earnout period, revenue from all Enterprise Customers of the Business that is recognized during such period',df.info['enterpriseToRevenue'])
               st.write("🔴 enterpriseToEbitda:  compares the value of a company—debt included—to the company's cash earnings less non-cash expenses",df.info['enterpriseToEbitda'])
     
     ######################################
     with st.expander("📊Technical Analysis"):
          st.header('📊Technical Analysis')

     #########################3
          df = hist 

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
          
          fig.update_xaxes(rangeslider_visible=True, rangeselector=dict(
          buttons=list([
               dict(count=1, label="1m", step="month", stepmode="backward"),
               dict(count=6, label="6m", step="month", stepmode="backward"),
               dict(count=1, label="YTD", step="year", stepmode="todate"),
               dict(count=1, label="1y", step="year", stepmode="backward"),
               dict(step="all")
          ])))
          
          st.plotly_chart(fig)
     
