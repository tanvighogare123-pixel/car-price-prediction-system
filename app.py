import streamlit as st

st.title("Car Price Prediction 🚗")

st.write("Welcome to my project")

year = st.number_input("Enter car year", 2000, 2025)
price = st.number_input("Enter present price")
kms = st.number_input("Enter kms driven")

if st.button("Predict"):
    st.success("Prediction coming soon 🚀")
