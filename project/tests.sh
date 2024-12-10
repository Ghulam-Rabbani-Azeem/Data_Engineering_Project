#!/bin/bash

# Activate virtual environment
source .venv/Scripts/activate

# Ensure dependencies are installed from requirements.txt
pip install -r requirements.txt

# Run the pipeline to ensure it produces output
echo "Running the data pipeline..."
python pipeline.py

# Run the tests with detailed output
echo "Running system tests with pytest..."
pytest -s system-test.py --maxfail=1 --disable-warnings --tb=short -q

# Exit with the status of pytest
exit $?

