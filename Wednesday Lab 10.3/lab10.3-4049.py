#TASK 1:AI-Assisted Bug Detection 
def factorial(n):
    result = 1
    for i in range(1,n):
        result = result * i
    return result
n = int(input("Enter a number: "))
print("Factorial of", n, "is", factorial(n))
# Prompt : Identify the logical error in the above code and correct it and explain why the error occurs and also provide a corrected version and also compare the both codes with comments.
# The logical error in the above code is that the loop runs from 1 to n-1, which means it does not include n in the multiplication. This results in an incorrect factorial calculation for n greater than 1.
# The corrected version of the code should run the loop from 1 to n (inclusive) to ensure that n is included in the multiplication.
# Corrected version:
def factorial(n):
    result = 1
    for i in range(1, n + 1):  # Loop runs from 1 to n (inclusive)
        result = result * i
    return result
n = int(input("Enter a number: "))
print("Factorial of", n, "is", factorial(n))
# Comparison of both codes:
# Original code:
# def factorial(n):
#     result = 1
#     for i in range(1,n):  # Loop runs from 1 to n-1
#         result = result * i
#     return result 
# In the original code, if n is 5, the loop will multiply 1 * 2 * 3 * 4, which results in 24 instead of 120 (5! = 120).
# Corrected code:
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):  # Loop runs from 1 to n (inclusive)
#         result = result * i
#     return result
# In the corrected code, if n is 5, the loop will multiply 1 * 2 * 3 * 4 * 5, which results in the correct factorial value of 120.

#TASK 2:Improving Readability & Documentation 
#Manual code:
def calc(a,b,c):
    if c == "add":
        return a + b
    elif c == "sub":
        return a - b
    elif c == "mul":
        return a * b
    elif c == "div":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (add, sub, mul, div): ")
result = calc(a, b, operation)
print("Result:", result)
#Rewrite the above function with descriptive function and parameters names with a complete docstring and exception handling for division by zero.
#AI code:
def calculate(num1, num2, operation):
    """
    Perform a basic arithmetic operation on two numbers.

    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): The operation to perform. It can be 'add', 'sub', 'mul', or 'div'.

    Returns:
    float: The result of the arithmetic operation.
    str: An error message if the operation is invalid or if division by zero occurs.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "sub":
        return num1 - num2
    elif operation == "mul":
        return num1 * num2
    elif operation == "div":
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation. Please choose from 'add', 'sub', 'mul', or 'div'."
# Example usage:
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operation = input("Enter operation (add, sub, mul, div): ")
result = calculate(number1, number2, operation)
print("Result:", result)

#TASK 3: Enforcing Coding Standards - PEP8 Compliance

# Original code with PEP8 violations:
def Checkprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
# Generate the code List all PEP8 voilations in the above code and refactor the code and Write a short note on how automated AI reviews could streamlinecode reviews in large teams.

# PEP8 Violations identified:
# 1. Function name uses PascalCase instead of snake_case
# 2. Missing docstring
# 3. Logic error: Does not check if n <= 1 (not prime by definition)
# 4. Inefficient: Should check only up to sqrt(n)

# Test cases for original function:
print("Testing original function:")
print(f"Checkprime(2): {Checkprime(2)}")  # Expected: True, Gets: True
print(f"Checkprime(4): {Checkprime(4)}")  # Expected: False, Gets: False
print(f"Checkprime(1): {Checkprime(1)}")  # Expected: False, Gets: True (WRONG!)
print(f"Checkprime(0): {Checkprime(0)}")  # Expected: False, Gets: True (WRONG!)

# PEP8-compliant and corrected version:
def check_prime(n):
    Check if a number is prime.
    
    Parameters:
    n (int): The number to check for primality.
    
    Returns:
    bool: True if n is prime, False otherwise.
 if n < 2:
        return False
 for i in range(2, int(n ** 0.5) + 1):
     if n % i == 0:
         return False
 return True

# Test cases for corrected function:
print("\nTesting corrected function:")
print(f"check_prime(2): {check_prime(2)}")    # Expected: True
print(f"check_prime(4): {check_prime(4)}")    # Expected: False
print(f"check_prime(1): {check_prime(1)}")    # Expected: False
print(f"check_prime(0): {check_prime(0)}")    # Expected: False
print(f"check_prime(17): {check_prime(17)}")  # Expected: True
print(f"check_prime(20): {check_prime(20)}")  # Expected: False

# Note on AI-assisted code reviews for large teams:
# AI-powered code review tools streamline quality assurance by:
# 1. Automatically detecting PEP8 violations and style inconsistencies
# 2. Providing real-time suggestions before code submission
# 3. Reducing manual review time, allowing teams to focus on logic and architecture
# 4. Ensuring consistent coding standards across the entire codebase
# 5. Catching common bugs and inefficiencies (e.g., unnecessary iterations)
# 6. Generating documentation suggestions and format improvements
# 7. Scaling code reviews for large teams without additional overhead

# TASK 4: AI as a Code Reviewer in Real Projects

# Original code submitted by teammate:
def processData(d):
    return [x * 2 for x in d if x % 2 == 0]

# Manual Code Review - Issues Identified:
# 1. Readability: Vague function name 'processData' and parameter 'd'
# 2. Reusability: Hardcoded multiplier (2) and operation (even filtering)
# 3. No input validation: Will crash on non-list input or non-numeric elements
# 4. No documentation: Purpose unclear
# 5. No type hints: Reduces code clarity and IDE support
# 6. Edge cases not handled: Empty lists, None values, non-integer types

# Refactored version with AI feedback applied:

def transform_even_numbers(numbers: List[Union[int, float]], multiplier: int = 2) -> List[Union[int, float]]:
    """
    Filter even numbers from a list and multiply them by a given factor.
    
    Parameters:
    numbers (List[Union[int, float]]): Input list containing numeric values.
    multiplier (int): The factor to multiply even numbers by (default: 2).
    
    Returns:
    List[Union[int, float]]: A list of transformed even numbers.
    
    Raises:
    TypeError: If input is not a list or contains non-numeric elements.
    """
    if not isinstance(numbers, list):
        raise TypeError(f"Expected list, got {type(numbers).__name__}")
    
    if not numbers:
        return []
    
    result = []
    for num in numbers:
        if isinstance(num, (int, float)) and num % 2 == 0:
            result.append(num * multiplier)
        elif not isinstance(num, (int, float)):
            raise TypeError(f"List contains non-numeric element: {num}")
    
    return result

# Test cases:
print("Test 1 - Normal case:", transform_even_numbers([1, 2, 3, 4, 5, 6]))
print("Test 2 - Empty list:", transform_even_numbers([]))
print("Test 3 - Custom multiplier:", transform_even_numbers([2, 4, 6], multiplier=5))
print("Test 4 - Floats:", transform_even_numbers([2.0, 3.5, 4.0]))

# Reflection: AI as Code Reviewer - Standalone vs. Assistant
# 
# AI Should be an ASSISTANT, not a standalone reviewer:
# Strengths of AI as assistant:
# - Detects style violations and common patterns quickly
# - Suggests generalization and parameterization
# - Catches potential runtime errors (type mismatches, edge cases)
# - Improves consistency and follows standards (PEP8, naming conventions)
#
# Why AI alone is insufficient:
# - Cannot understand business logic or project-specific requirements
# - May miss architectural concerns or design patterns
# - Lacks context about performance trade-offs
# - Cannot evaluate code quality beyond syntax (e.g., algorithmic complexity)
# - Needs human judgment for acceptance criteria
#
# Recommendation:
# Use AI as a first-pass reviewer to catch mechanical issues, then have
# human reviewers focus on logic, design, and business impact.

#Task5:AI-Assisted Performance Optimization 
def sum_of_squares(numbers):
    total = 0
    for num in numbers:
        total += num ** 2
    return total
numbers = range(1000000)
#Optimized High-Performance Code with numpy
import numpy as np
def sum_of_squares(numbers):
    """
    Calculate the sum of squares of a list of numbers.

    Args:
        numbers (iterable): An iterable of numerical values.
    Returns:
        float: The sum of squares of the input numbers.
    """
    return np.sum(np.square(numbers))
numbers = np.arange(1000000)
#Execution time comparision code
import time
# Original code execution time
start_time = time.time()
numbers = range(1000000)
print(sum_of_squares(numbers))
end_time = time.time()
print(f"Original code execution time: {end_time - start_time} seconds")
# Optimized code execution time
start_time = time.time()
numbers = np.arange(1000000)
print(sum_of_squares(numbers))
end_time = time.time()
print(f"Optimized code execution time: {end_time - start_time} seconds")
