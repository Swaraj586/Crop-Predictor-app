import streamlit as st
import requests

API_URL = "https://crop-predictor-yb4j.onrender.com/predict"

st.title("Crop Predictor")

st.markdown("Enter the details below:")

nitrogen = st.number_input("Nitrogen content",min_value=1)
phosphorous = st.number_input("Phosphorous content",min_value=1)
potassium = st.number_input("Potassium content",min_value=1)
temperature = st.number_input("Temperature(in °C)",min_value=1.00,step=0.1,format="%.2f")
humidity = st.number_input("Humidity(in %)",min_value=1.00,max_value=100.0,step=0.1,format="%.2f")
ph = st.number_input("pH value of soil",min_value=1.00,step=0.1,format="%.2f")
rainfall = st.number_input("Rainfall(in mm)",min_value=1.00,step=0.1,format="%.2f")


if st.button("Predict Crop"):
    input_data = {
        "nitrogen" : nitrogen,
        "phosphorous" : phosphorous,
        "potassium" : potassium,
        "temperature" : temperature,
        "humidity" : humidity,
        "pH" : ph,
        "rainfall" : rainfall
    }

    try:
        response = requests.post(API_URL,json=input_data)
        if response.status_code==200:
            result = response.json()
            st.success(f"Predicted Crop: **{result['predicted_category']}**")
        else:
            st.error(f"API error : {response.status_code} - {response.text}")

    except requests.exceptions.ConnectionError:
        st.error("Could not connect to FastApi server!!!")