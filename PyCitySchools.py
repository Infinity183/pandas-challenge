# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas DataFrames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset.  
schools = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
schools.head()

total_schools = len(schools['school_name'].unique())
total_students = schools['student_name'].count()
total_budget = schools['budget'].unique().sum()
average_math_score = schools['math_score'].mean()
average_reading_score = schools['reading_score'].mean()
passing_math = len(schools[schools['math_score'] >= 70]) / total_students
passing_reading = len(schools[schools['reading_score'] >= 70]) / total_students
passing_both = len(schools[(schools['math_score'] >= 70) & (schools['reading_score'] >= 70)]) / total_students

data_list = [total_schools, total_students, total_budget, average_math_score, average_reading_score, passing_math, passing_reading, passing_both]
data_list

totals = pd.DataFrame({'Total Schools': [total_schools],'Total Students': [total_students],'Total Budget': [total_budget],'Average Math Score': [average_math_score],'Average Reading Score': [average_reading_score],'Percent Passing Math': [passing_math], 'Percent Passing Reading': [passing_reading],'Percent Passing Both': [passing_both]})
totals.style.format({'Total Students': '{:,.0f}'})
totals