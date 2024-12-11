#!/bin/bash

# Activate virtual environment
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source .venv/Scripts/activate
else
    source .venv/bin/activate
fi

# Ensure dependencies are installed
pip install -r requirements.txt

# Run the pipeline to ensure it produces output
echo "Running the data pipeline..."
python pipeline.py || exit 1

# Run the tests with detailed output
echo "Running system tests with pytest..."
pytest -s system-test.py --disable-warnings --tb=short -q

# Exit with the status of pytest
exit $?
