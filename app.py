import pandas as pd
import streamlit as st

# Load CSV and use the second row as header (header=1)
csv_file = "global_food_security.csv"
try:
    data = pd.read_csv(csv_file, header=1)
except FileNotFoundError:
    st.error(f"CSV file '{csv_file}' not found.")
    st.stop()

# Normalize column names: strip spaces and lowercase
data.columns = data.columns.str.strip().str.lower()

# Show columns
st.write("Columns in the dataset:", data.columns.tolist())

# Define target column
target_col = "affordability"

# Check if target column exists
if target_col not in data.columns:
    st.error(f"Column '{target_col}' not found in CSV. Available columns: {list(data.columns)}")
    st.stop()

# Calculate min and max for the target column
aff_min, aff_max = data[target_col].min(), data[target_col].max()

st.write(f"Minimum {target_col}: {aff_min}")
st.write(f"Maximum {target_col}: {aff_max}")

# Display the dataset
st.dataframe(data)
