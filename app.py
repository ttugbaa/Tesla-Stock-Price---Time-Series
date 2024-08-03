import streamlit as st
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose

# Create the Streamlit app
st.title("	:chart_with_downwards_trend: Stock Price Decomposition :chart_with_upwards_trend: ")

# Allow the user to upload the CSV file
uploaded_file = st.file_uploader("Please upload a CSV file containing the stock data.", type="csv")

if uploaded_file is not None:
    # Load the stock data from the uploaded file
    df = pd.read_csv(uploaded_file)

    # Convert the 'Date' column to a DatetimeIndex
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    # Perform seasonal decomposition
    decomposition = seasonal_decompose(df['Close'], model='additive', period=30)
    trend = decomposition.trend
    seasonal = decomposition.seasonal
    residual = decomposition.resid

    # Display the decomposition results
    st.subheader("Trend")
    st.line_chart(trend)

    st.subheader("Seasonal")
    st.line_chart(seasonal)

    st.subheader("Residual")
    st.line_chart(residual) 