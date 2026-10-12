
import pandas as pd
import numpy as np

# Load the student dataset
students = pd.read_csv("students.csv")

# Validate the required columns
required_columns = [
    "Student_ID",
    "Name",
    "Department",
    "Python",
    "Data_Analysis",
    "AI",
    "Attendance"
]

missing_columns = [
    column for column in required_columns
    if column not in students.columns
]

if missing_columns:
    raise ValueError(
        f"Missing required columns in students.csv: {missing_columns}"
    )

print("Dataset validation successful!")


# Validate required data
numeric_columns = [
    "Python",
    "Data_Analysis",
    "AI",
    "Attendance"
]

# Check for missing values
if students[required_columns].isnull().any().any():
    raise ValueError("The dataset contains missing values.")

# Check that marks and attendance are numeric
for column in numeric_columns:
    students[column] = pd.to_numeric(
        students[column],
        errors="raise"
    )

# Check that marks and attendance are between 0 and 100
if not students[numeric_columns].apply(
    lambda column: column.between(0, 100).all()
).all():
    raise ValueError(
        "Marks and attendance must be between 0 and 100."
    )

print("Data validation successful!")

# Display the student data
print("Student Dataset:")
print(students)

# Display the number of students
print("\nNumber of Students:")
print(len(students))

# Display the column names
print("\nColumn Names:")
print(students.columns)

# Display basic information about the dataset
print("\nDataset Information:")
students.info()

# Calculate total marks
students["Total_Marks"] = (
    students["Python"]
    + students["Data_Analysis"]
    + students["AI"]
)

print("\nTotal Marks:")
print(students[["Student_ID", "Name", "Total_Marks"]])

# Calculate average marks
students["Average_Marks"] = students["Total_Marks"] / 3

print("\nAverage Marks:")
print(students[["Student_ID", "Name", "Average_Marks"]])

# Function to calculate grade
def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# Assign grades to students
students["Grade"] = students["Average_Marks"].apply(calculate_grade)

print("\nStudent Grades:")
print(students[["Student_ID", "Name", "Average_Marks", "Grade"]])

# Function to determine pass or fail
def check_result(row):
    if row["Average_Marks"] >= 40 and row["Attendance"] >= 75:
        return "PASS"
    else:
        return "FAIL"


# Assign pass/fail status
students["Result"] = students.apply(check_result, axis=1)

print("\nStudent Results:")
print(
    students[
        ["Student_ID", "Name", "Average_Marks", "Attendance", "Grade", "Result"]
    ]
)

# Calculate overall class statistics
class_average = students["Average_Marks"].mean()
highest_average = students["Average_Marks"].max()
lowest_average = students["Average_Marks"].min()

pass_count = (students["Result"] == "PASS").sum()
fail_count = (students["Result"] == "FAIL").sum()

print("\nClass Statistics:")
print("Overall Class Average:", round(class_average, 2))
print("Highest Average:", round(highest_average, 2))
print("Lowest Average:", round(lowest_average, 2))
print("Number of Passed Students:", pass_count)
print("Number of Failed Students:", fail_count)

# Calculate subject-wise averages
python_average = students["Python"].mean()
data_analysis_average = students["Data_Analysis"].mean()
ai_average = students["AI"].mean()

print("\nSubject-wise Averages:")
print("Python:", round(python_average, 2))
print("Data Analysis:", round(data_analysis_average, 2))
print("AI:", round(ai_average, 2))

# Display the top 5 performers
top_performers = students.sort_values(
    by="Average_Marks",
    ascending=False
).head(5)

print("\nTop 5 Performers:")
print(
    top_performers[
        ["Student_ID", "Name", "Department", "Average_Marks", "Grade"]
    ].round({"Average_Marks": 2})
)

# Calculate subject averages using NumPy
subject_marks = students[["Python", "Data_Analysis", "AI"]].to_numpy()

numpy_subject_averages = np.mean(subject_marks, axis=0)

# Display subject averages using a for loop
subjects = ["Python", "Data Analysis", "AI"]

print("\nSubject Averages Using NumPy:")

for index in range(len(subjects)):
    print(f"{subjects[index]}: {numpy_subject_averages[index]:.2f}")

# Analyze performance by department
department_performance = students.groupby("Department")[
    ["Python", "Data_Analysis", "AI", "Average_Marks"]
].mean()

print("\nDepartment-wise Performance:")
print(department_performance.round(2))

# Analyze student attendance
average_attendance = students["Attendance"].mean()

low_attendance = students[students["Attendance"] < 75]

print("\nAttendance Analysis:")
print(f"Average Attendance: {average_attendance:.2f}%")
print(f"Students with Attendance Below 75%: {len(low_attendance)}")

print("\nLow Attendance Students:")
print(low_attendance[["Student_ID", "Name", "Attendance"]])

# Save the analyzed student data to a CSV file
students.to_csv("student_performance_report.csv", index=False)

print("\nStudent performance report saved successfully!")