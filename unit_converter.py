import streamlit as st

# Title of the app
st.set_page_config(page_title="Unit Converter", layout="centered")
st.title("Unit Converter")

# Description of the app
st.write("This is a unit converter app built with Streamlit.")

# User input for conversion category
conversion_category = st.selectbox("Select conversion category:", ["Length", "Area", "Mass", "Pressure", "Speed"])

# User input for units based on selected category
if conversion_category == "Length":
    unit_from = st.selectbox("Select unit to convert from:", ["Meters", "Kilometers", "Miles", "Feet"])
    unit_to = st.selectbox("Select unit to convert to:", ["Meters", "Kilometers", "Miles", "Feet"])
elif conversion_category == "Area":
    unit_from = st.selectbox("Select unit to convert from:", ["Square Meters", "Hectares", "Acres"])
    unit_to = st.selectbox("Select unit to convert to:", ["Square Meters", "Hectares", "Acres"])
elif conversion_category == "Mass":
    unit_from = st.selectbox("Select unit to convert from:", ["Grams", "Kilograms", "Pounds", "Ounces"])
    unit_to = st.selectbox("Select unit to convert to:", ["Grams", "Kilograms", "Pounds", "Ounces"])
elif conversion_category == "Pressure":
    unit_from = st.selectbox("Select unit to convert from:", ["Pascals", "Bar", "PSI"])
    unit_to = st.selectbox("Select unit to convert to:", ["Pascals", "Bar", "PSI"])
elif conversion_category == "Speed":
    unit_from = st.selectbox("Select unit to convert from:", ["Meters per second", "Kilometers per hour", "Miles per hour"])
    unit_to = st.selectbox("Select unit to convert to:", ["Meters per second", "Kilometers per hour", "Miles per hour"])

value = st.number_input("Enter the value to convert:")

# Conversion logic
def convert_units(value, unit_from, unit_to, category):
    conversion_factors = {
        "Length": {
            "Meters": 1,
            "Kilometers": 0.001,
            "Miles": 0.000621371,
            "Feet": 3.28084
        },
        "Area": {
            "Square Meters": 1,
            "Hectares": 0.0001,
            "Acres": 0.000247105
        },
        "Mass": {
            "Grams": 1,
            "Kilograms": 0.001,
            "Pounds": 0.00220462,
            "Ounces": 0.035274
        },
        "Pressure": {
            "Pascals": 1,
            "Bar": 0.00001,
            "PSI": 0.000145038
        },
        "Speed": {
            "Meters per second": 1,
            "Kilometers per hour": 3.6,
            "Miles per hour": 2.23694
        }
    }
    
    if unit_from != unit_to:
        value_in_base = value / conversion_factors[category][unit_from]
        converted_value = value_in_base * conversion_factors[category][unit_to]
        return round(converted_value, 2)  # Round off the result to 2 decimal places
    else:
        return value

# Perform conversion and display result
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to, conversion_category)
    st.markdown(f"<div style='background-color: green; padding: 10px; color: white; border-radius: 5px;'>"
                 f"{value} {unit_from} is equal to {result} {unit_to}.</div>", unsafe_allow_html=True)
