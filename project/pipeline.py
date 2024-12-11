import os
import pandas as pd
import sqlite3

# Constants
DATA_DIR = ".\data"
DATASET_1 = "alistairking/renewable-energy-consumption-in-the-u-s"
DATASET_2 = "abdelrahman16/co2-emissions-usa"
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
data_path_1 = os.path.join(DATA_DIR, "emissions.csv")
data_path_2 = os.path.join(DATA_DIR, "dataset.csv")

# Read datasets
data = pd.read_csv(data_path_1)
additional_data = pd.read_csv(data_path_2)

# Print both data sets tables of five values each before modifications
print("Data (Renewable Energy Consumption) preview:")
print(data.head(5))

print("\nAdditional Data (CO2 Emissions) preview:")
print(additional_data.head(5))

# Check column names
print("\nData columns:", data.columns)
print("Additional data columns:", additional_data.columns)

# Process the additional dataset
# Ensure the column 'Year' exists before processing
if 'Year' in additional_data.columns:
    additional_data_annual = additional_data.groupby("Year").sum(numeric_only=True).reset_index()
    
    # Rename 'Year' column if necessary to match data DataFrame
    additional_data_annual.rename(columns={'Year': 'year'}, inplace=True)

    # Merge the datasets
    merged_data = pd.merge(data, additional_data_annual, left_on="year", right_on="year", how="inner")
    print("\nMerged data preview:")
    print(merged_data.head())
    print("\nMerged data columns:", merged_data.columns)

    # Select relevant columns
    columns_to_keep = [
        "year", "state-name", "sector-name", "fuel-name", "value"  # Update based on what columns are in merged_data
    ]

    # Verify filtered data
    try:
        filtered_data = merged_data[columns_to_keep]
        print("\nFiltered data preview:")
        print(filtered_data.head())

        # Save processed data to SQLite
        with sqlite3.connect(DB_PATH) as conn:
            filtered_data.to_sql("renewable_energy", conn, if_exists="replace", index=False)
            print(f"Data saved to SQLite database at {DB_PATH}")

            # Verify saved data in database
            query = "SELECT * FROM renewable_energy LIMIT 5"
            result = pd.read_sql(query, conn)
            print("\nData from SQLite:")
            print(result)
    except KeyError as e:
        print(f"KeyError: {e}. Check column names in merged_data.")
else:
    print("The 'Year' column is missing from the additional data. Please check the column names.")
