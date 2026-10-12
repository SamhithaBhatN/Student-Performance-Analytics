# Student Performance Analytics System

## Project Overview

The Student Performance Analytics System is a Python-based project developed as part of the **Python with AI Internship at EWB Edu Tech Private Limited**.

The project analyzes student academic performance using Python, Pandas, and NumPy. It calculates total and average marks, assigns grades, determines pass/fail results, analyzes subject-wise and department-wise performance, identifies top performers, and generates a CSV report.

## Objectives

* Analyze student academic performance using a structured dataset.
* Calculate total and average marks for each student.
* Assign grades based on average marks.
* Determine pass/fail results using academic performance and attendance.
* Calculate class-level and subject-wise statistics.
* Compare performance across departments.
* Identify the top five performers.
* Export the analyzed results to a CSV file.

## Features

* **Dataset Loading:** Reads student records from a CSV file using Pandas.
* **Data Validation:** Checks required columns, missing values, numeric data, and valid mark and attendance ranges.
* **Student Statistics:** Calculates total marks and average marks for each student.
* **Grade Calculation:** Assigns grades based on student averages.
* **Pass/Fail Analysis:** Determines results based on average marks and attendance.
* **Class Performance Analysis:** Calculates the overall class average, highest average, lowest average, and pass/fail counts.
* **Subject-wise Analysis:** Calculates average marks in Python, Data Analysis, and AI.
* **Top Performers:** Identifies the top five students based on average marks.
* **NumPy Analysis:** Uses NumPy to calculate subject averages.
* **Department-wise Analysis:** Compares average performance across departments.
* **Attendance Analysis:** Calculates average attendance and identifies students with attendance below 75%.
* **CSV Report Generation:** Exports the analyzed student data to a new CSV file.

## Technologies Used

* **Python 3.11** — Core programming language.
* **Pandas** — Dataset loading, processing, grouping, and analysis.
* **NumPy** — Numerical calculations and subject-wise averages.
* **CSV** — Input dataset and output report format.
* **Visual Studio Code** — Development environment.
* **Git and GitHub** — Version control and project hosting.

## Dataset Details

The project uses `students.csv`, which contains 20 student records.

| Column        | Description                           |
| ------------- | ------------------------------------- |
| Student_ID    | Unique identifier for each student    |
| Name          | Student name                          |
| Department    | Student's academic department         |
| Python        | Python subject marks                  |
| Data_Analysis | Data Analysis subject marks           |
| AI            | Artificial Intelligence subject marks |
| Attendance    | Attendance percentage                 |

### Calculation Rules

**Total Marks**

Total marks are calculated by adding marks in Python, Data Analysis, and AI.

`Total_Marks = Python + Data_Analysis + AI`

**Average Marks**

The average is calculated by dividing total marks by the three subjects.

`Average_Marks = Total_Marks / 3`

**Grade Criteria**

| Average Marks  | Grade |
| -------------- | ----- |
| 90 and above   | A+    |
| 80 to below 90 | A     |
| 70 to below 80 | B     |
| 60 to below 70 | C     |
| 50 to below 60 | D     |
| Below 50       | F     |

**Pass/Fail Criteria**

A student receives `PASS` when their average marks are at least 40 and attendance is at least 75%. Otherwise, the result is `FAIL`.

These are the grading and result rules implemented in the current program.

## Installation and Setup

### Prerequisites

* Python 3.11 or later
* pip (Python package installer)

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd Student-Performance-Analytics
```

Replace `<your-github-repository-url>` with your actual GitHub repository URL.

### 2. Install Dependencies

Install the required Python libraries:

```bash
pip install pandas numpy
```

### 3. Run the Project

Ensure that `students.csv` and `main.py` are in the same directory. Then run:

```bash
python main.py
```

### 4. Generated Report

After successful execution, the program generates:

`student_performance_report.csv`

The report contains the original student information along with calculated total marks, average marks, grades, and pass/fail results.

## Sample Results

The program analyzes 20 student records and produces the following summary:

| Metric                  | Result |
| ----------------------- | -----: |
| Total Students          |     20 |
| Overall Class Average   |  72.80 |
| Highest Student Average |  93.67 |
| Lowest Student Average  |  42.00 |
| Students Passed         |     18 |
| Students Failed         |      2 |
| Average Attendance      | 86.35% |

### Top Five Performers

| Student | Average Marks | Grade |
| ------- | ------------: | ----- |
| Meera   |         93.67 | A+    |
| Aisha   |         92.00 | A+    |
| Rohan   |         91.33 | A+    |
| Neha    |         89.67 | A     |
| Sneha   |         89.00 | A     |

*These results are based on the current sample dataset.*

## Project Structure

```text
Student-Performance-Analytics/
├── main.py
├── students.csv
├── student_performance_report.csv
└── README.md
```

## Learning Outcomes

Through this project, the following concepts are applied:

* Python functions, conditional statements, and loops.
* Reading and validating CSV data.
* Pandas DataFrames and data manipulation.
* NumPy numerical operations.
* Statistical summaries and grouped analysis.
* Sorting and identifying top-performing students.
* Exporting analyzed data to CSV.

## Future Enhancements

* Add graphical charts for subject-wise and department-wise performance.
* Build an interactive dashboard to explore student results.
* Add more datasets and configurable grading criteria.

## Author

Developed as part of the Python with AI Internship at EWB Edu Tech Private Limited.
