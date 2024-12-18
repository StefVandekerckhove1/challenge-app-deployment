import streamlit as st
import numpy as np
import pandas as pd
from preprocessing.cleaning_data import preprocess
from predict.prediction import predict

df = pd.read_csv("preprocessing/data/real_estate_belgium.csv")

st.title("Welcome on the ImmoEliza prediction model")

# Description
st.write("""
Enter the details of the house to estimate its price.  
This app is powered by xgboost trained on housing market data.
""")

st.write("""
Provide the details of the property to predict its estimated value or potential ROI.
""")

# User Inputs for all features
st.header("Property Details")

# 1. Enter the municipality
# Municipality = st.text_input("Give Municipality:")

col_one_list = df['Municipality'].unique().tolist()
Municipality = st.selectbox('Select the Municipality', col_one_list)

# 2. Room and living area Combined
Number_of_rooms = int(st.number_input("Number of Bedrooms", min_value=1, max_value=50, step=1))
Living_area = int(st.number_input("Livable Space (sq meters)", min_value=10, max_value=5000, step=1))

# 3. Outside Area
Garden_area = int(st.number_input("Garden Area (sq meters)", min_value=0, max_value=1000, step=1))
Terrace_area = int(st.number_input("Terrace Area (sq meters)", min_value=0, max_value=25000, step=1))

# 4. Kitchen (Binary Encoding)
Fully_equipped_kitchen = st.radio(
    "Does the property have a fully equipped kitchen?",
    ["Yes", "No"]
)
if Fully_equipped_kitchen == "Yes":
    kitchen_encoded = 1
else:  
    kitchen_encoded = 0


# 5. Type of property

type_of_property = st.radio(
    "House or appartment?", ["House","Appartment"])

if type_of_property == "House":
    Type_of_Property = 0
else:
    Type_of_Property = 1

# Predict button
if st.button("Predict Price"):
    try:
        # Preprocess input data
        input_data = {
            "Municipality" : Municipality, 
            "Living_Area" : Living_area, 
            "Number_of_Rooms" : Number_of_rooms, 
            "Fully_Equipped_Kitchen" : kitchen_encoded, 
            "Terrace_Area" : Terrace_area, 
            "Garden_Area" : Garden_area,  
            "Type_of_Property" : Type_of_Property
        }
        predicted_price = predict(input_data)
        st.success(f"The predicted price is €{predicted_price:,.2f}")
    except ValueError as e:
         st.error(f"Error: {e}")