import pandas as pd
import numpy as np

# Create a list of integers
list1 = [1, 2, 3]

# Convert the list to a NumPy array
list1_ndarray = np.array(list1)  # prints out: [1, 2, 3]

# Convert the NumPy array to a Pandas Series
list1_series = pd.Series(list1_ndarray)

# list1_series prints out:

# 0    1
# 1    2
# 2    3
# dtype: int32

# Create a list of ages
ages = [40, 37, 10]

# Create a corresponding list of names
names = ['Eric', 'Ivy', 'Jude']

# Convert the ages list to a NumPy array
ages_array = np.array(ages)  # prints out: [40, 37, 10]

# Convert the ages NumPy array to a Pandas Series with names as the index
ages_series = pd.Series(ages, index=names)

# ages_series prints out:

# Eric    40
# Ivy     37
# Jude    10
# dtype: int64

# Create a list of lists representing student data
students = [
    ['Eric', 40, 'Machine Learning'],
    ['Ivy', 37, 'Project Management'],
    ['Jude', 10, 'Programmer']
]

# Define the column names for the DataFrame
columns = ['Name', 'Age', 'Course']

# Create a Pandas DataFrame from the students list with the specified columns
students_dataframe = pd.DataFrame(students, columns=columns)

# students_dataframe prints out:

#    Name  Age              Course
# 0  Eric   40    Machine Learning
# 1   Ivy   37  Project Management
# 2  Jude   10          Programmer

# Set the 'Name' column as the index of the DataFrame
students_dataframe.set_index('Name', inplace=True)

# students_dataframe prints out:

#       Age              Course
# Name
# Eric   40    Machine Learning
# Ivy    37  Project Management
# Jude   10          Programmer


# Creating a DataFrame by passing a dictionary of objects where the keys are the column
# labels and the values are the column values.

friends_dataf = pd.DataFrame({
    'Name': ['Eric', 'Ivy', 'Jude'],
    'Age': [40, 37, 10]
}).set_index('Name')

# friends_dataf prints out:

#       Age              Course
# Name
# Eric   40    Machine Learning
# Ivy    37  Project Management
# Jude   10          Programmer
