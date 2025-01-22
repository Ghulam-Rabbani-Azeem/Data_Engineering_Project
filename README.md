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

## Project Overview  
This project focuses on the development of a robust data pipeline to analyze renewable energy consumption and its relationship to carbon dioxide (CO₂) emissions in the United States. The goal is to uncover actionable insights and provide dynamic visualizations for stakeholders through an interactive dashboard.

[**Project Repository**](https://github.com/Ghulam-Rabbani-Azeem/Data_Engineering_Project): Explore code, workflows, and dataset processing pipeline.

[**Pipeline Script**](pipeline.py): Automates data processing, transformation, and database population.

[**Automated Test Suite**](system-test.py): Ensures the reliability and correctness of the pipeline using system-level validations.

---

## Project Structure  

- **`pipeline.py`**: Automates data downloading, cleaning, and processing for renewable energy analysis.
- **`pipeline.sh`**: Shell script for running the pipeline script.
- **`test.sh`**: Manages environment setup, runs the pipeline, and executes system tests.
- **`.github/workflows/CI.yml`**: Automates Continuous Integration (CI) testing on GitHub.
- **`requirements.txt`**: Lists all Python dependencies for the project.
  
---

## Continuous Integration Workflow  

The GitHub Actions workflow in `CI.yml` automates the following steps:

1. **Setup Environment**  
   - Checkout the repository.  
   - Install Python 3.10 and dependencies.  

2. **Run Tests**  
   - Execute `test.sh` to validate the pipeline’s functionality.

3. **Kaggle API Configuration**  
   - Uses GitHub secrets to access Kaggle datasets automatically.  

4. **Validate Pipeline**  
   - Executes data pipeline and tests end-to-end operations.  

---

## Automated Testing  

The `system-test.py` script performs automated testing to verify the integrity of the pipeline. Key tests include:

- **Data Directory Verification**: Ensures the `data` directory is present.  
- **Dataset Availability**: Confirms required datasets exist in the specified paths.  
- **Data Readability**: Checks for successful loading of datasets into pandas DataFrames.  
- **Database Creation**: Verifies the SQLite database generation.  
- **Database Validation**: Ensures the `renewable_energy` table is populated with data.

---

## Shell Scripts Description  

### `test.sh`  

1. Activates the virtual environment (`.venv/Scripts/activate`).  
2. Installs dependencies from `requirements.txt`.  
3. Runs the data pipeline via `pipeline.py`.  
4. Executes system tests using `pytest`.  

### `pipeline.sh`  

1. Runs the data processing pipeline using `pipeline.py`.  
2. Displays a completion message once the pipeline execution is finished.

---

## Renewable Energy Dashboard Overview  

1. **Dashboard Functionality**  
   - Interactive visualizations of renewable energy trends.  
   - Displays KPIs for energy usage and emissions.

2. **Key Features**  
   - Renewable energy trends by year, state, and sector.  
   - Sector-wise and state-wise breakdowns of energy usage and emissions.  
   - Responsive filtering with dropdown selectors for specific insights.

3. **Technology Used**  
   - Built using Dash and Plotly for visualizations.  
   - Styled with Dash Bootstrap components for a professional look.  
   - SQLite database for efficient data storage and retrieval.

4. **Simulated Data**  
   - Adds additional state-sector-year combinations for expanded analysis.








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
