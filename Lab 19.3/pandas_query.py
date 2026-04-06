#Task 1 – Python to C++ Conversion
'''Task:
Translate a simple Python class into C++ using AI assistance.
Instructions:
• Prompt AI to convert a Python class representing a Student
with attributes and methods into equivalent C++ code
• Ensure proper handling of:
o Constructors
o Data types
o Access specifiers
• Compile and run both versions to verify output consistency
Expected Output:
An equivalent working C++ class translated from Python.'''
import pandas as pd

# Sample DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'salary': [45000, 55000, 60000, 48000, 70000],
    'department': ['HR', 'IT', 'IT', 'Finance', 'IT']
}
df = pd.DataFrame(data)

# Equivalent Pandas query
result = df[df['salary'] > 50000][['name', 'salary']]

print("Original DataFrame:")
print(df)
print("\nFiltered Result (salary > 50000):")
print(result)
