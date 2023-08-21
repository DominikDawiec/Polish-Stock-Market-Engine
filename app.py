# Imports

# Data processing libraries
import pandas as pd
import yfinance as yf

# Visualization libraries
import plotly.graph_objs as go

# Streamlit and other utilities
import streamlit as st

# Configuration

st.set_page_config(layout="centered", page_icon="📈", page_title="Polish Stock Market App")
st.title("📈 Polish Stock App")

# Functions

def create_stock_plot(hist):
    """Create a figure with historical stock data."""
    fig = go.Figure()

    trace_configs = [
        ('Open', 'rgb(5, 177, 59)'),
        ('Low', 'rgb(50, 30, 197)'),
        ('High', 'rgb(243, 187, 112)'),
        ('Close', 'rgb(193, 8, 0)')
    ]

    for trace, color in trace_configs:
        fig.add_trace(go.Scatter(
            x=hist.index,
            y=hist[trace],
            mode='lines',
            name=trace,
            line_color=color
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

def display_company_details(df_info):
    """Display company details."""
    st.header("📝 Company's details")
    details = [
        ("Full name:", df_info['longName']),
        ("Sector:", df_info['sector']),
        ("Industry:", df_info['industry']),
        ("Country:", df_info['country']),
        ("City:", df_info['city']),
        ("Address:", df_info['address1']),
        ("Zip:", df_info['zip']),
        ("Summary:", df_info['longBusinessSummary']),
        ("Website:", df_info['website'])
    ]
    for name, value in details:
        st.write(f"{name} {value}")

def display_kpis(df_info):
    """Display Key Performance Indicators."""
    st.header('🎯 Key Performance Indicators')
    kpis = [
        # ... (as in your original code)
    ]
    for name, value in kpis:
        st.write(name, value)

def technical_analysis(hist):
    """Perform and display technical analysis."""
    # ... (as in your original code)
    fig = go.Figure()
    # ... (rest of your technical analysis visualization)
    st.plotly_chart(fig)

# Main Application Logic

companies = ['CDR.WA', 'KER.WA', 'KGH.WA', 'ALE.WA']

with st.sidebar:
    option = st.selectbox('Please select company', companies)

if option:
    df = yf.Ticker(option)
    hist = df.history(period="max")

    tab1, tab2 = st.tabs(["Plot", "Raw Data"])

    with tab1:
        create_stock_plot(hist)

    with tab2:
        st.dataframe(hist)

    with st.expander("📝 Company's details"):
        display_company_details(df.info)

    with st.expander("🎯 Key Performance Indicators"):
        display_kpis(df.info)

    with st.expander("📊 Technical Analysis"):
        technical_analysis(hist)
