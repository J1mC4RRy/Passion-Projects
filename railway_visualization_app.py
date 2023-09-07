import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv('synthetic_railway_dataset.csv')

df = load_data()

# Title
st.title("Synthetic Railway Dataset Visualizations")

# 1. Histogram for Ticket_Price
st.subheader("1. Histogram for Ticket Prices")
ticket_prices = df['Ticket_Price']
fig1 = px.histogram(ticket_prices, nbins=20, labels={'value': 'Ticket Prices'})
st.plotly_chart(fig1)

# 2. Bar chart: Average ticket price per Origin
st.subheader("2. Average Ticket Price per Origin")
avg_price_per_origin = df.groupby('Origin').Ticket_Price.mean().reset_index()
fig2 = px.bar(avg_price_per_origin, x='Origin', y='Ticket_Price', labels={'Ticket_Price': 'Average Price'})
st.plotly_chart(fig2)

# 3. Pie chart for seats distribution by Origin
st.subheader("3. Seats Distribution by Origin")
seats_by_origin = df.groupby('Origin').Seats_Available.sum().reset_index()
fig3 = px.pie(seats_by_origin, names='Origin', values='Seats_Available', title='Seats by Origin')
st.plotly_chart(fig3)

# 4. Scatter plot: Departure_Time vs. Ticket_Price
st.subheader("4. Scatter Plot: Departure Time vs. Ticket Price")
df['Hour'] = pd.to_datetime(df['Departure_Time']).dt.hour
fig4 = px.scatter(df, x='Hour', y='Ticket_Price', labels={'Hour': 'Departure Hour', 'Ticket_Price': 'Price'})
st.plotly_chart(fig4)
