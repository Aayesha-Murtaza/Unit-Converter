import streamlit as st

# Set up page
st.set_page_config(page_title="Unit Converter", layout="centered")
st.title("Unit Converter")
st.write("A simple unit conversion tool built with Streamlit.")

# Define conversion factors globally
conversion_factors = {
    "Length": {"Meters": 1, "Kilometers": 0.001, "Miles": 0.000621371, "Feet": 3.28084},
    "Area": {"Square Meters": 1, "Hectares": 0.0001, "Acres": 0.000247105},
    "Mass": {"Grams": 1, "Kilograms": 0.001, "Pounds": 0.00220462, "Ounces": 0.035274},
    "Pressure": {"Pascals": 1, "Bar": 0.00001, "PSI": 0.000145038},
    "Speed": {"Meters per second": 1, "Kilometers per hour": 3.6, "Miles per hour": 2.23694},
}

# Select conversion category
category = st.selectbox("Select conversion category:", list(conversion_factors.keys()))

# Dynamically populate unit options
units = list(conversion_factors[category].keys())
unit_from = st.selectbox("Convert from:", units)
unit_to = st.selectbox("Convert to:", units)
value = st.number_input("Enter value to convert:", min_value=0.0, format="%.2f")

# Conversion function
def convert_units(value, unit_from, unit_to, category):
    if unit_from == unit_to:
        return value
    base_value = value / conversion_factors[category][unit_from]
    return round(base_value * conversion_factors[category][unit_to], 2)

# Perform conversion
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to, category)
    st.success(f"{value} {unit_from} is equal to {result} {unit_to}")
