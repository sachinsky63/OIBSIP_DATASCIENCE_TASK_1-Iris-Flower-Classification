
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("car_price_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="centered"
)

st.title("🚗 Car Price Prediction")
st.write("Enter car details to predict its selling price.")

# Input fields
brand = st.selectbox(
    "Car Brand",
    ["Maruti", "Hyundai", "Honda", "Tata", "Toyota",
     "Mahindra", "Ford", "Renault", "Volkswagen", "Other"]
)

car_age = st.slider("Car Age (Years)", 0, 30, 5)
km_driven = st.number_input(
    "Kilometers Driven",
    min_value=0,
    value=50000,
    step=1000
)

fuel = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "Cng", "Lpg", "Electric"]
)

seller_type = st.selectbox(
    "Seller Type",
    ["Individual", "Dealer", "Trustmark Dealer"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic"]
)

owner = st.selectbox(
    "Owner",
    ["First Owner", "Second Owner", "Third Owner",
     "Fourth & Above Owner", "Test Drive Car"]
)

# Prediction button
if st.button("Predict Car Price"):
    try:
        input_data = pd.DataFrame([{
            "brand": brand,
            "car_age": car_age,
            "km_driven": km_driven,
            "fuel": fuel,
            "seller_type": seller_type,
            "transmission": transmission,
            "owner": owner
        }])

        prediction = model.predict(input_data)[0]

        st.success(
            f"Estimated Selling Price: ₹{prediction:,.0f}"
        )
        st.caption("This is an estimated price, not a guaranteed market value.")

    except Exception as e:
        st.error(f"Prediction failed: {e}")

