# Data Science Project - README

## Table of Contents
- [Course Organization](#course-organization)
- [Project Work](#project-work)
  - [Project Work 1 - Set Up Project](#project-work-1---set-up-project)
  - [Project Work 2 - Project Plan](#project-work-2---project-plan)
  - [Project Work 3 - Data Pipeline](#project-work-3---data-pipeline)
  - [Project Work 4 - Data Report](#project-work-4---data-report)
  - [Project Work 5 - Automated Testing](#project-work-5---automated-testing)
  - [Project Work 6 - CI](#project-work-6---ci)
  - [Project Work 7 - Final Report](#project-work-7---final-report)
  - [Project Work 8 - Presentation](#project-work-8---presentation)
- [Exercises](#exercises)
  - [Exercise 1](#exercise-1)
  - [Exercise 2](#exercise-2)
  - [Exercise 3](#exercise-3)
  - [Exercise 4](#exercise-4)
  - [Exercise 5](#exercise-5)

---

## Project Work

You will develop an individual data science project over the course of the semester. The project is self-organized and should relate to **"The Americas"** (North-, Middle-, or South-America). It must be based on at least **two different open data sources.**

### Open Data Sources (Suggestions)
- [Mobilithek](https://mobilithek.info/)
- [European Data Portal](https://www.europeandataportal.eu/)
- [GovData](https://www.govdata.de/)
- [Awesome Public Datasets (GitHub)](https://github.com/awesomedata/awesome-public-datasets)

> **⚠️ Important:** Do not use APIs that require continuous crawling. Only use static datasets that can be downloaded once.

### Technology Stack
- Use **Python LTS** or **Jayvee** for your project.
- The goal is to create a **report** that answers an interesting question based on your data sources.

---

## Project Work Tasks

### Project Work 1 - Set Up Project
- Fork the repository template: [made-template](https://github.com/jvalue/made-template)
- (Optional) Rename your repository
- Submit the repository link via [Google Form](https://forms.gle/N8ev7giukG86EtZd8)
- Set up your development environment ([Jayvee Docs](https://jvalue.github.io/jayvee/))

### Project Work 2 - Project Plan
- Submit `project-plan.md` in the `/project` directory.
- Create GitHub issues to outline work packages.
- Explore your chosen datasets.

### Project Work 3 - Data Pipeline
- Build an automated data pipeline.
- Store processed datasets in `/data` directory.
- Write a script (Python or Jayvee) to pull, transform, and clean data.
- Add a pipeline entry script `/project/pipeline.sh`.

```bash
#!/bin/bash
python3 /project/pipeline.py
```

### Project Work 4 - Data Report
- **Mandatory Submission** (Failure results in failing the course).
- Submit `data-report.pdf` (max. 3 pages) in `/project`.
- Describe datasets, licenses, pipeline process, and quality analysis.

### Project Work 5 - Automated Testing
- Add `/project/tests.sh` to run automated tests.
- Include at least **one system-level test**.
- Validate pipeline output files exist.

### Project Work 6 - CI (Continuous Integration)
- Add GitHub Actions workflow to run tests on every push.
- Use `tests.sh` to verify functionality.
- Avoid exposing private keys/passwords.

### Project Work 7 - Final Report
- **Mandatory Submission** (Failure results in failing the course).
- Submit `analysis-report.pdf` (max. 4 pages) in `/project`.
- Must include **Introduction, Data Used, Analysis, and Conclusions**.
- Use figures/tables to present findings.

### Project Work 8 - Presentation
- Update **README.md** with title & project description.
- Choose an **open-source license** (e.g., CC BY 4.0).
- (Optional) Submit a **presentation**:
  - `/project/slides.pdf`
  - `/project/presentation-video.md` (link to video)
- **Bonus:** Present live (Zoom session selection is random).

---

## Exercises

> **📝 Note:** Submit exercises in `/exercises` as `exercise<number>.jv` (e.g., `/exercises/exercise1.jv`).

### Exercise 1
- Process airports dataset from: [Open Data](https://opendata.rhein-kreis-neuss.de/api/explore/v2.1/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv)
- Save as `airports.sqlite` (table: `airports`)
- Use Jayvee **0.6.3**

### Exercise 2
- Process tree planting dataset: [GovData](https://www.govdata.de/web/guest/suchen/-/details/stadt-neuss-baumpflanzungen-2023)
- Save as `trees.sqlite` (table: `trees`)
- Use Jayvee **0.6.3**

### Exercise 3
- Extract World Bank dataset: [Metadata](https://datacatalog.worldbank.org/search/dataset/0061114/World-Development-Report-2022)
- Extract **"Figure S5.1.2"** from Excel.
- Save as `country-stats.sqlite`:
  - Table `bondIssuance` (Country Code, Bond Issuance Share)
  - Table `gdpPerCapita` (Country Code, GDP per Capita)
- Use Jayvee **0.6.4**

### Exercise 4
- Process temperature dataset: [Mobilithek](https://mobilithek.info/offers/526718847762190336)
- Convert temperatures **Celsius → Fahrenheit**.
- Save as `temperatures.sqlite` (table: `temperatures`)
- Use Jayvee **0.6.4**

### Exercise 5
- Process GTFS transit data: [GTFS.zip](https://gtfs.rhoenenergie-bus.de/GTFS.zip)
- Extract `stops.txt` (filter zone **1925**)
- Save as `gtfs.sqlite` (table: `stops`)
- Use Jayvee **0.6.4**

---

## Additional Resources
- [Jayvee Documentation](https://jvalue.github.io/jayvee/)
- [Jayvee GitHub](https://github.com/jvalue/jayvee)
- [Course Forum](https://www.studon.fau.de/frm5003028.html)

🚀 **Happy Coding!**

