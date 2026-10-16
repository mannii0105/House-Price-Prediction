import streamlit as st
import pandas as pd
import joblib


# Load trained model
model = joblib.load("models/house_price_model.pkl")


# Page title
st.title("🏠 House Price Prediction")


st.write(
    "Enter the details of the house below to predict its price."
)


# User inputs
gr_liv_area = st.number_input(
    "Living Area (sq ft)",
    min_value=100,
    max_value=10000,
    value=2000
)

bedrooms = st.number_input(
    "Number of Bedrooms",
    min_value=0,
    max_value=10,
    value=3
)

full_bath = st.number_input(
    "Full Bathrooms",
    min_value=0,
    max_value=10,
    value=2
)

half_bath = st.number_input(
    "Half Bathrooms",
    min_value=0,
    max_value=10,
    value=1
)

overall_qual = st.number_input(
    "Overall Quality (1-10)",
    min_value=1,
    max_value=10,
    value=7
)

year_built = st.number_input(
    "Year Built",
    min_value=1800,
    max_value=2026,
    value=2015
)

garage_cars = st.number_input(
    "Garage Capacity",
    min_value=0,
    max_value=10,
    value=2
)

total_bsmt_sf = st.number_input(
    "Basement Area (sq ft)",
    min_value=0,
    max_value=10000,
    value=800
)


# Prediction button
if st.button("Predict House Price"):

    # Create input data
    new_house = pd.DataFrame([{
        "GrLivArea": gr_liv_area,
        "BedroomAbvGr": bedrooms,
        "FullBath": full_bath,
        "HalfBath": half_bath,
        "OverallQual": overall_qual,
        "YearBuilt": year_built,
        "GarageCars": garage_cars,
        "TotalBsmtSF": total_bsmt_sf
    }])

    # Make prediction
    prediction = model.predict(new_house)[0]

    # Display result
    st.success(
        f"Estimated House Price: ${prediction:,.2f}"
    )