import pandas as pd

# Create a list of lists representing student data
students = [
    ['Eric', 40, 'Machine Learning'],
    ['Ivy', 37, 'Project Management'],
    ['Jude', 10, 'Programmer'],
    ['Alice', 22, 'Data Science'],
    ['Bob', 25, 'Web Development'],
    ['Charlie', 23, 'Cyber Security'],
    ['Diana', 28, 'AI and Robotics'],
    ['Edward', 21, 'Cloud Computing'],
    ['Fiona', 24, 'Software Engineering']
]

# Define the column names for the DataFrame
columns = ['Name', 'Age', 'Course']

# Create an index for the DataFrame
index = [list(range(1, len(students) + 1))]

# Create a Pandas DataFrame from the students list with the specified columns and index
students_df = pd.DataFrame(students, columns=columns, index=index)

# Print the DataFrame will look like this:
#       Name  Age                Course
# 1     Eric   40      Machine Learning
# 2      Ivy   37    Project Management
# 3     Jude   10            Programmer
# 4    Alice   22          Data Science
# 5      Bob   25       Web Development
# 6  Charlie   23        Cyber Security
# 7    Diana   28       AI and Robotics
# 8   Edward   21       Cloud Computing
# 9    Fiona   24  Software Engineering


# Preview the top 5 rows of the DataFrame (default behavior)

preview_head_default = students_df.head()

# This will print the top 5 rows:
#       Name  Age                Course
# 1     Eric   40      Machine Learning
# 2      Ivy   37    Project Management
# 3     Jude   10            Programmer
# 4    Alice   22          Data Science
# 5      Bob   25       Web Development


# Preview the top 2 rows of the DataFrame

preview_head_defined = students_df.head(2)

# This will print the top 2 rows:
#       Name  Age                Course
# 1     Eric   40      Machine Learning
# 2      Ivy   37    Project Management


# Preview the bottom 5 rows of the DataFrame (default behavior)

preview_tail_default = students_df.tail()

# This will print the bottom 5 rows:
#       Name  Age                Course
# 5      Bob   25       Web Development
# 6  Charlie   23        Cyber Security
# 7    Diana   28       AI and Robotics
# 8   Edward   21       Cloud Computing
# 9    Fiona   24  Software Engineering


# Preview the bottom 2 rows of the DataFrame

preview_tail_defined = students_df.tail(2)

# This will print the bottom 2 rows:
#      Name  Age                Course
# 8  Edward   21       Cloud Computing
# 9   Fiona   24  Software Engineering


# Convert the DataFrame to a NumPy array

students_df_to_numpy = students_df.to_numpy()

# This will print the DataFrame as a NumPy array:
# [['Eric' 40 'Machine Learning']
#  ['Ivy' 37 'Project Management']
#  ['Jude' 10 'Programmer']
#  ['Alice' 22 'Data Science']
#  ['Bob' 25 'Web Development']
#  ['Charlie' 23 'Cyber Security']
#  ['Diana' 28 'AI and Robotics']
#  ['Edward' 21 'Cloud Computing']
#  ['Fiona' 24 'Software Engineering']]


# Generate descriptive statistics of the DataFrame

describe_students_df = students_df.describe()

# This will print out descriptive statistics for the 'Age' column:
#              Age
# count   9.000000
# mean   25.555556
# std     8.875685
# min    10.000000
# 25%    22.000000
# 50%    24.000000
# 75%    28.000000
# max    40.000000


# Transpose the DataFrame

transpose_students_df = students_df.T

# This will transpose the DataFrame (swap rows and columns):
#                        1  ...                     9
# Name                Eric  ...                 Fiona
# Age                   40  ...                    24
# Course  Machine Learning  ...  Software Engineering


# Sort the DataFrame columns in descending order

sort_by_index_students_df = students_df.sort_index(axis=1, ascending=False)

# This will sort the columns in descending order:
#       Name                Course  Age
# 1     Eric      Machine Learning   40
# 2      Ivy    Project Management   37
# 3     Jude            Programmer   10
# 4    Alice          Data Science   22
# 5      Bob       Web Development   25
# 6  Charlie        Cyber Security   23
# 7    Diana       AI and Robotics   28
# 8   Edward       Cloud Computing   21
# 9    Fiona  Software Engineering   24


# Sort the DataFrame rows by the 'Age' column in descending order

sort_by_value_students_df = students_df.sort_values(by='Age', ascending=False)

# This will sort the rows by 'Age' in descending order:
#       Name  Age                Course
# 1     Eric   40      Machine Learning
# 2      Ivy   37    Project Management
# 7    Diana   28       AI and Robotics
# 5      Bob   25       Web Development
# 9    Fiona   24  Software Engineering
# 6  Charlie   23        Cyber Security
# 4    Alice   22          Data Science
# 8   Edward   21       Cloud Computing
# 3     Jude   10            Programmer
