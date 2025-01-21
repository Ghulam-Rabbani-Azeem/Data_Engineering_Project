
# Analyzing the Impact of Renewable Energy Adoption on U.S. Carbon Emissions  

<img src="image.jpg" width="900" height="400"> 

## Project Overview  
This project investigates the relationship between renewable energy adoption across different sectors and states in the U.S. and its impact on carbon dioxide (CO₂) emissions. By analyzing data on renewable energy consumption and emissions, we aim to uncover trends, correlations, and actionable insights to inform sustainable development strategies.  

[**Project Report**](project/report.ipynb): Analyze datasets to derive key findings and create visual representations.  

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
