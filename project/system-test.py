import os
import sqlite3
import pandas as pd
import pytest

# Constants
DATA_DIR = "./data"  # Use relative path for portability
DB_PATH = os.path.join(DATA_DIR, "renewable_energy.sqlite3")
DATASET_1_PATH = os.path.join(DATA_DIR, "emissions.csv")
DATASET_2_PATH = os.path.join(DATA_DIR, "dataset.csv")

# Custom test report handler to print the outcome of each test
def pytest_runtest_logreport(report):
    if report.when == "call" and report.outcome == "passed":
        print(f"Passed: {report.nodeid}")
    elif report.when == "call" and report.outcome == "failed":
        print(f"Failed: {report.nodeid}")

# Test if the data directory exists
def test_data_directory_exists():
    """Test if the data directory is created."""
    print("Running test: test_data_directory_exists")
    assert os.path.exists(DATA_DIR), f"Data directory {DATA_DIR} does not exist."

# Test if both datasets exist
def test_datasets_exist():
    """Test if the datasets have been downloaded."""
    print("Running test: test_datasets_exist")
    
    # Assert that dataset 1 exists
    assert os.path.isfile(DATASET_1_PATH), f"Dataset 1 not found at {DATASET_1_PATH}"
    
    # Assert that dataset 2 exists
    assert os.path.isfile(DATASET_2_PATH), f"Dataset 2 not found at {DATASET_2_PATH}"

# Test if both datasets can be read into DataFrames
def test_datasets_are_readable():
    """Test if the datasets can be read into DataFrames."""
    print("Running test: test_datasets_are_readable")
    try:
        data = pd.read_csv(DATASET_1_PATH)
        additional_data = pd.read_csv(DATASET_2_PATH)
    except Exception as e:
        assert False, f"Error reading datasets: {e}"
    
    # Check that neither of the datasets is empty
    assert not data.empty, "Dataset 1 is empty."
    assert not additional_data.empty, "Dataset 2 is empty."

# Test if the SQLite database is created
def test_sqlite_database_creation():
    """Test if the SQLite database is created."""
    print("Running test: test_sqlite_database_creation")
    assert os.path.isfile(DB_PATH), f"SQLite database {DB_PATH} does not exist."

# Test if the SQLite table contains data
def test_sqlite_table_contains_data():
    """Test if the SQLite database contains data."""
    print("Running test: test_sqlite_table_contains_data")
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM renewable_energy")
            count = cursor.fetchone()[0]
    except Exception as e:
        assert False, f"Error querying SQLite database: {e}"
    
    # Check if the table contains more than 0 rows
    assert count > 0, "SQLite database table `renewable_energy` is empty."
