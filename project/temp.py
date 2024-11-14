
import os
from urllib.request import urlopen
import io
import pandas as pd

# Replace these with URLs pointing to actual raw CSV files
data_urls=["https://www.eia.gov/totalenergy/data/browser/csv.php?tbl=T10.01",
           "https://www.statista.com/statistics/224747/renewable-energy-production-and-consumption-in-the-us/"]

# Function to download and parse data from a URL
def download_data(url, header='infer', skiprows=None):
    try:
        response = urlopen(url)  # Fetch the content of the URL
        data = response.read().decode('utf-8')  # Decode bytes to a string
        # Read the data into a pandas DataFrame
        df = pd.read_csv(io.StringIO(data), header=header, skiprows=skiprows)
        print(f"Downloaded data from {url}:")
        return df
    except Exception as e:
        print(f"Error downloading data from {url}: {e}")
        return pd.DataFrame()

def main():
    for i, url in enumerate(data_urls):  # Loop through the list of URLs
        if i == 0:  # First dataset
            df = download_data(url, header=1)  # Use second row as header
            if not df.empty:
                print(df.head())  # Display the first few rows
        else:  # Second dataset
            df = download_data(url)  # Default header behavior
            if not df.empty:
                print(df.head())  # Display the first few rows

if __name__ == "__main__":
    main()
