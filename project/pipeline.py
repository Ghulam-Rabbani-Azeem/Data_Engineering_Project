import os
import pandas as pd
import sqlite3

# Constants
DATA_DIR = "D:\\AllProjects\\made-template\\data"
DATASET_1 = "alistairking/renewable-energy-consumption-in-the-u-s"
DATASET_2 = "anishvijay/global-renewable-energy-and-indicators-dataset"
DB_PATH = os.path.join(DATA_DIR, "renewable_energy.sqlite3")

# Create the data directory
os.makedirs(DATA_DIR, exist_ok=True)

# Function to download datasets using the Kaggle API
def download_dataset(dataset, path):
    os.system(f"kaggle datasets download -d {dataset} -p {path} --unzip")

# Download the datasets
download_dataset(DATASET_1, DATA_DIR)
download_dataset(DATASET_2, DATA_DIR)

# Load the datasets
data_path_1 = os.path.join(DATA_DIR, "complete_renewable_energy_dataset.csv")
data_path_2 = os.path.join(DATA_DIR, "dataset.csv")

data = pd.read_csv(data_path_1)
additional_data = pd.read_csv(data_path_2)

# Check column names
print("Data columns:", data.columns)
print("Additional data columns:", additional_data.columns)

# Process the additional dataset
additional_data_annual = additional_data.groupby("Year").sum(numeric_only=True).reset_index()

# Verify the merged data
merged_data = pd.merge(data, additional_data_annual, on="Year", how="inner")
print("Merged data preview:", merged_data.head())

# Select relevant columns
columns_to_keep = [
    "Year", "Energy Type", "Production (GWh)", "Installed Capacity (MW)",
    "Population", "GDP", "CO2 Emissions", "Proportion of Energy from Renewables"
]

# Verify filtered data
filtered_data = merged_data[columns_to_keep]
print("Filtered data preview:", filtered_data.head())

# Save processed data to SQLite
with sqlite3.connect(DB_PATH) as conn:
    filtered_data.to_sql("renewable_energy", conn, if_exists="replace", index=False)
    print(f"Data saved to SQLite database at {DB_PATH}")

    # Verify saved data in database
    query = "SELECT * FROM renewable_energy LIMIT 5"
    result = pd.read_sql(query, conn)
    print("Data from SQLite:", result)
