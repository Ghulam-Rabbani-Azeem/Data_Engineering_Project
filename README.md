<table style="border: none; width: 100%; text-align: center;">
  <tr style="border: none;">
    <td style="border: none;">
      <h1>Analyzing the Impact of Renewable Energy Adoption on U.S.</h1>
      <h1>Carbon Emissions</h1>
    </td>
  </tr>
</table>


<img src="image.png" width="1000" height="300"> 

## Project Overview  
This project investigates the relationship between renewable energy adoption across different sectors and states in the U.S. and its impact on carbon dioxide (CO₂) emissions. By analyzing data on renewable energy consumption and emissions, we aim to uncover trends, correlations, and actionable insights to inform sustainable development strategies.  

[**Project Report**](project/analysis-report.pdf): Analyze datasets to derive key findings and create visual representations.  

[**Presentation Slides**](project/slides.pptx): Summary of findings in a concise format.  

[**Presentation Video Link**](project/presentation-video.md): Detailed video presentation of the project.  

---

## Datasets  

1. **[Renewable Energy Consumption in the U.S.](Renewable Energy Data)**  
   - Metadata: [Renewable Energy Metadata](Renewable Energy Metadata)  
   - Type: CSV  

2. **[CO₂ Emissions in the U.S.](CO₂ Emissions Data)**  
   - Metadata: [CO₂ Emissions Metadata](CO₂ Emissions Metadata)  
   - Type: CSV  

---

## Tools and Technologies Used  
- **Data Analysis**: Python (Pandas, NumPy)  
- **Visualization**: Matplotlib, Seaborn  

---

## Installation and Usage  
Follow these steps to set up the project environment and run the analysis scripts:  

```bash  
# Clone the repository  
git clone https://github.com/Ghulam-Rabbani-Azeem/Data_Engineering_Project 

# Navigate into the project repository folder  
cd project  

# Install dependencies  
pip install -r requirements.txt  

### Project Structure  

The following key files and scripts are present in the project folder:  
- `pipeline.py`: The Python script containing the automated data pipeline for downloading, cleaning, and processing datasets.  
- `pipeline.sh`: A shell script to execute the `pipeline.py` script.  
- `test.sh`: A shell script to set up the environment, ensure dependencies are installed, run the pipeline, and execute system tests with `pytest`.  
- `.github/workflows/CI.yml`: A GitHub Actions workflow for continuous integration, ensuring automated tests are executed on every push to the `main` branch.  
- `requirements.txt`: A list of required Python packages for the project.  

## Continuous Integration Workflow  

The GitHub Actions workflow file (`CI.yml`) automates testing, ensuring consistent validation of the pipeline after every code change. It performs the following steps:  
1. **Checkout Repository**: Downloads the project files from the repository.  
2. **Set up Python Environment**: Installs Python 3.10.  
3. **Install Dependencies**: Installs project requirements using `pip`.  
4. **Configure Kaggle API**: Sets up Kaggle credentials (stored as GitHub secrets) for dataset downloads.  
5. **Run Tests**: Executes the `test.sh` script to validate the pipeline.

## Description of Shell Scripts  

### `test.sh`  
The `test.sh` script performs the following actions:  
1. Activates the virtual environment using `.venv/Scripts/activate`.  
2. Ensures that all dependencies listed in `requirements.txt` are installed.  
3. Runs the data pipeline by executing the `pipeline.py` script to produce outputs.  
4. Executes system tests using `pytest` with detailed output, halting after the first failure.  
5. Exits with the status code from `pytest` to signal success or failure.  

### `pipeline.sh`  
The `pipeline.sh` script is a simplified tool to execute the data pipeline. It performs the following actions:  
1. Runs the `pipeline.py` script.  
2. Displays a message indicating that the data pipeline execution is completed.  

These scripts provide flexibility in managing the data pipeline and ensure robust testing and execution for consistent results.
## Automated Testing (system-test.py)

Automated testing is integral to ensuring the robustness and accuracy of the pipeline. The `system-test.py` script validates key components of the pipeline, including:

- **Data Directory Verification:** Ensures that the `data` directory exists.
- **Dataset Availability:** Confirms the presence of required datasets in the specified paths.
- **Data Readability:** Verifies that datasets are not corrupted and can be read into pandas DataFrames.
- **SQLite Database Creation:** Ensures the SQLite database is generated successfully.
- **Database Content Validation:** Checks that the `renewable_energy` table in the SQLite database is populated with data.


## Renewable Energy Dashboard Code Details  

### Key Features  

1. **Data Loading and Transformation**  
   - Reads data from an SQLite database (`renewable_energy.sqlite3`) containing renewable energy and CO₂ emissions statistics.  
   - Simulates additional data to expand the dataset using the function `create_expanded_dataset()`.

2. **Dashboard Initialization**  
   - Uses the `Dash` framework for creating interactive web applications.  
   - Applies `dash-bootstrap-components` for consistent and responsive UI styling.  
   - Utilizes `Plotly` for creating interactive graphs.

3. **Dynamic Graphs and KPIs**  
   - **KPI Cards:**  
     - Displays metrics for total renewable energy usage and the years of data available.  
   - **Graphs:**  
     - Renewable Energy Trends (line graph by year and energy type).  
     - Top States by Energy Usage (bar graph of top 10 states).  
     - Sector-Wise Energy Distribution (pie chart for energy usage by sector).  
     - Year-Wise Renewable Energy Trends (bar chart showing yearly totals).  
     - State-Year Comparison (grouped bar chart for state emissions and renewable energy).

4. **Filtering Options**  
   - Dropdown filters allow users to select specific states and sectors, dynamically updating graphs and KPIs.

5. **Interactive Graphs**  
   - Visualizations respond to user input in real time, enhancing data exploration.

6. **Data Simulation**  
   - Adds state-sector-year data for more comprehensive analysis.








# Methods of Advanced Data Engineering Template Project

This template project provides some structure for your open data project in the MADE module at FAU.
This repository contains (a) a data science project that is developed by the student over the course of the semester, and (b) the exercises that are submitted over the course of the semester.

To get started, please follow these steps:
1. Create your own fork of this repository. Feel free to rename the repository right after creation, before you let the teaching instructors know your repository URL. **Do not rename the repository during the semester**.

## Project Work
Your data engineering project will run alongside lectures during the semester. We will ask you to regularly submit project work as milestones, so you can reasonably pace your work. All project work submissions **must** be placed in the `project` folder.

### Exporting a Jupyter Notebook
Jupyter Notebooks can be exported using `nbconvert` (`pip install nbconvert`). For example, to export the example notebook to HTML: `jupyter nbconvert --to html examples/final-report-example.ipynb --embed-images --output final-report.html`


## Exercises
During the semester you will need to complete exercises using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.jv`.

In regular intervals, exercises will be given as homework to complete during the semester. Details and deadlines will be discussed in the lecture, also see the [course schedule](https://made.uni1.de/).

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). 

To view your exercise feedback, navigate to Actions → Exercise Feedback in your repository.

The exercise feedback is executed whenever you make a change in files in the `exercise` folder and push your local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, open the `exercise-feedback` job and `Exercise Feedback` step. You should see command line output that contains output like this:

```sh
Found exercises/exercise1.jv, executing model...
Found output file airports.sqlite, grading...
Grading Exercise 1
	Overall points 17 of 17
	---
	By category:
		Shape: 4 of 4
		Types: 13 of 13
```
