Task 4 – SQL to Pandas Query

Task:
Translate a SQL query into a Pandas DataFrame operation in Python.

Instructions:
• Provide AI with a SQL query (e.g., SELECT name, salary FROM employees WHERE salary > 50000).
• Ask AI to generate equivalent Pandas code.
• Test the generated code on a sample DataFrame.

Expected Output:
• Equivalent Pandas query that retrieves the correct subset of data.

SQL Query:
```sql
SELECT name, salary FROM employees WHERE salary > 50000;
```

Pandas Code (pandas_query.py):
```python
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
```

Verification:
The Pandas code filters the DataFrame for salaries greater than 50000 and selects only name and salary columns, matching the SQL query.
