import streamlit as st
from model import train_model, predict_next_month
from utils import load_data

st.set_page_config(page_title="Smart Inventory Tool", layout="centered")

st.title("📦 Smart Inventory Optimization Tool")

uploaded_file = st.file_uploader("Upload a CSV file (product, month, sales)", type="csv")

if uploaded_file:
    df = load_data(uploaded_file)
    st.write("### Uploaded Data", df)

    for product in df['product'].unique():
        st.subheader(f"📊 Predictions for Product: {product}")
        prod_df = df[df['product'] == product]
        last_month = prod_df['month'].max()
        model = train_model(prod_df)
        prediction = predict_next_month(model, last_month)
        st.success(f"📈 Predicted demand for month {last_month + 1}: {round(prediction)} units")
