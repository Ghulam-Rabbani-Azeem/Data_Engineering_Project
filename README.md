# Renewable Energy and CO₂ Emissions Analysis Project

<img src="image.png" width="700" height="466">

## Project Overview  
This project investigates the relationship between renewable energy adoption across different sectors and states in the U.S. and its impact on carbon dioxide (CO₂) emissions. The goal is to analyze trends, uncover correlations, and provide actionable insights to support sustainable development strategies.

[**Pipeline Script**](pipeline.py): Automates data processing, transformation, and database loading.  

[**Automated Testing Suite**](system-test.py): Ensures pipeline integrity with system-level validations.  

[**GitHub Workflow**](.github/workflows/CI.yml): Automates CI testing with GitHub Actions.  

---

### Datasets  
1. [**Emissions Dataset**](data/emissions.csv): Includes carbon dioxide emissions data for various sectors across U.S. states.  
2. [**Renewable Energy Dataset**](data/dataset.csv): Contains renewable energy usage statistics across multiple states and sectors.  

Both datasets are preprocessed and stored in a SQLite database (`renewable_energy.sqlite3`) for analysis.  

---

## Tools and Technologies Used  
- **Programming**: Python (Pandas, SQLite, Plotly, Dash)  
- **Visualization**: Plotly, Dash Bootstrap Components  
- **Automation**: GitHub Actions  
- **Database**: SQLite  

---

## Installation and Setup  

Follow these steps to set up the project:  

```bash
# Clone the repository
git clone https://github.com/Ghulam-Rabbani-Azeem/Data_Engineering_Project.git

# Navigate to the project folder
cd Data_Engineering_Project

# Install dependencies
pip install -r requirements.txt
