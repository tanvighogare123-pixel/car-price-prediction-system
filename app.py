import streamlit as st
import pandas as pd
import numpy as np

st.title("Car Price Prediction 🚗")

st.write("Enter car details:")

year = st.number_input("Year", 2000, 2025)
present_price = st.number_input("Present Price")
kms_driven = st.number_input("Kms Driven")

if st.button("Predict"):
    st.success("Prediction feature coming soon 🚀")
