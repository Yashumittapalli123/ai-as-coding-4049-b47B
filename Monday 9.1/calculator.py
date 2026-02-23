#Task 3:
# Problem 3: Calculator (Automatic Documentation Generation)
#Create a Python module calculator.py that includes thefollowing functions, each written with appropriate docstrings: o add(a, b) – returns the sum of two numberso subtract(a, b) – returns the difference of two numberso multiply(a, b) – returns the product of two numberso divide(a, b) – returns the quotient of two numbers.
def add(a, b):
    """
    Returns the sum of two numbers.

    Parameters:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The sum of a and b.
    """
    return a + b
def subtract(a, b):
    """
    Returns the difference of two numbers.

    Parameters:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The difference of a and b.
    """
    return a - b
def multiply(a, b):
    """
    Returns the product of two numbers.

    Parameters:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The product of a and b.
    """
    return a * b
def divide(a, b):
    """
    Returns the quotient of two numbers.

    Parameters:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The quotient of a and b. If b is zero, returns 'Error: Division by zero'.
    """
    if b == 0:
        return 'Error: Division by zero'
    return a / b


