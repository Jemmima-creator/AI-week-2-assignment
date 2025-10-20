AI  Assignment


📁 Project Overview

Project Name: Global Food Security Dashboard

Student Name: Jemmimah Mwithalii

Course: Artificial Intelligence 

Objective:

Analyze global food security data from a CSV file.

Identify key statistics, such as minimum and maximum values for affordability.

Visualize the dataset interactively using Streamlit.

🌱 Relevance to Sustainable Development Goals (SDG)

This project supports SDG 2: Zero Hunger, which aims to end hunger, achieve food security, improve nutrition, and promote sustainable agriculture.

Affordability Analysis: Identifies countries where food is least affordable, helping policymakers focus on improving access to nutritious food.

Availability Insights: Shows which regions have better food availability, informing strategies for distribution and supply chain improvements.

Quality & Safety Metrics: Highlights the nutritional quality and safety of food across different countries, supporting global food safety standards.

Interactive Visualization: Enables stakeholders, researchers, and governments to make data-driven decisions toward achieving SDG 2 targets.

By analyzing global food security metrics, this project helps raise awareness of food access disparities and supports initiatives to improve nutrition and food affordability worldwide.

📂 Dataset

File: global_food_security.csv

Source: Global Food Security Index

Description: The dataset contains rankings of countries based on multiple food security indicators.

Key Columns:

Country – Name of the country

Overall Score – Total food security score

Affordability – Affordability metric for food

Availability – Food availability metric

Quality & Safety – Quality and safety metric

Notes:

The CSV has a first row that can be ignored; the second row contains column headers.

Column names may contain spaces and uppercase letters; the code normalizes them to lowercase for consistency.

⚙️ Requirements

Install the necessary Python packages:

pip install pandas streamlit plotly

📝 Code Structure

app.py – Main Streamlit application file

Loads the CSV dataset

Normalizes column names

Checks for the existence of the affordability column

Calculates min and max affordability

Displays the dataset in an interactive table

Visualizes data with bar, line, and scatter charts

global_food_security.csv – Dataset file

🚀 How to Run the App

Ensure both app.py and global_food_security.csv are in the same folder.

Open a terminal/command prompt in the project folder.

Run the following command:

streamlit run app.py


The app will open in a browser window. You will see:

Available columns in the dataset

Minimum and maximum affordability values

Interactive dataset table

Charts visualizing key metrics

📈 Key Features

Dynamic CSV Loading

Automatically reads the dataset and adjusts for header rows.

Column Validation

Checks if the target column (affordability) exists.

Shows available columns if missing.

Data Statistics

Calculates minimum and maximum values for affordability.



Error Handling

Alerts if CSV is missing or columns are not found.






📊 Expected Outputs

Minimum affordability: 15.8

Maximum affordability: 98.9

Interactive dataset table showing all countries and scores.
