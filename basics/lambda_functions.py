"""
In Python, a lambda function is a one-line shorthand for a function.

Example: add_two = lambda my_input: my_input + 2
"""

# Define a lambda function named 'is_substring'
is_substring = lambda my_string: my_string in "This is the master string"

# Description:
# The 'is_substring' function checks if the given string 'my_string' is a substring of the fixed string
# "This is the master string".

# Parameters:
# my_string (str): The string to check for being a substring.

# Returns:
# bool: Returns True if 'my_string' is found within "This is the master string", otherwise returns False.


# Define a lambda function named 'check_adult'
check_adult = lambda age: "Adult" if age >= 18 else "Not an adult"

# Description:
# The 'check_adult' function determines if a person is an adult based on their age.
# It uses a lambda function to check if the given 'age' is 18 or older.

# Parameters:
# age (int): The age of the person to check.

# Returns:
# str: Returns "Adult" if the age is 18 or older, otherwise returns "Not an adult".
