#TASK 1
A.#generate a documentaion for the functions def find_max(numbers),return max(numbers) with docstring documentation.
'''def find_max(numbers):
    """
    This function takes a list of numbers as input and returns the maximum number from the list.

    Parameters:
    numbers (list): A list of numerical values.

    Returns:
    The maximum number from the input list.
    """
    return max(numbers) 

B.#generate a documentaion for the function  def find_max(numbers),return max(numbers) with inline comments.
def find_max(numbers):
    # This function takes a list of numbers as input
    # and returns the maximum number from the list.
    
    # Use the built-in max() function to find and return the maximum number
    return max(numbers)
C.#generate  a documentaion for the function  def find_max(numbers),return max(numbers) with google style documentation.
def find_max(numbers):
    """
    Finds the maximum number in a list of numbers.

    Args:
        numbers (list): A list of numerical values.
    Returns:
        The maximum number from the input list.
    """    
    return max(numbers)
'''

# Comparison of documentation styles:
# (a) Docstring:
# Advantages:
# - Provides a clear and structured way to document the function.
# - Can be easily accessed using the help() function in Python.
# Disadvantages:
# - May be overlooked by developers who are not familiar with the format.
# Suitable use cases:
# - Ideal for documenting functions, classes, and modules in Python.
# (b) Inline comments:
# Advantages:
# - Provides immediate context and explanations for specific lines of code.
# Disadvantages:
# - Can clutter the code if overused, making it harder to read.
# Suitable use cases:
# - Best for explaining complex logic or specific implementation details within the code.
# (c) Google-style documentation:
# Advantages:
# - Provides a clear and consistent format for documenting code, making it easier to read and understand
# Disadvantages:
# - May require more effort to maintain and update compared to inline comments.
# Suitable use cases:
# - Ideal for larger projects or libraries where consistent documentation is crucial for maintainability.
# Recommendation:
# For a mathematical utilities library, the Google-style documentation is most effective. This is because it provides a consistent and readable format that is widely recognized and supported by tools like Sphinx, making it easier for developers to understand and maintain the library.


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#TASK 2:
A.#generate a documentation for  Python function def login(user, password, credentials) ,return credentials.get(user) == password with docstring documentation.
def login(user, password, credentials):
    """
    This function checks if the provided user credentials are valid.

    Parameters:
    user (str): The username to be authenticated.
    password (str): The password to be authenticated.
    credentials (dict): A dictionary containing username-password pairs.

    Returns:
    bool: True if the credentials are valid, False otherwise.
    """
    return credentials.get(user) == password
B.#generate a documentation for  Python function def login(user, password, credentials) ,return credentials.get(user) == password with inline comments.
def login(user, password, credentials):
    # This function checks if the provided user credentials are valid.
    
    # Use the get() method of the credentials dictionary to retrieve the password for the given user
    # and compare it with the provided password. Return True if they match, otherwise return False.
    return credentials.get(user) == password
C.#generate a documentation for  Python function def login(user, password, credentials) ,return credentials.get(user) == password with google style documentation.
def login(user, password, credentials):
    """
    Authenticates a user based on provided credentials.

    Args:
        user (str): The username to be authenticated.
        password (str): The password to be authenticated.
        credentials (dict): A dictionary containing username-password pairs.

    Returns:
        bool: True if the credentials are valid, False otherwise.
    """
    return credentials.get(user) == password

# 2. Comparison of documentation styles:
# (a) Docstring:
# Advantages:
# - Provides a clear and structured way to document the function.
# - Can be easily accessed using the help() function in Python.
# Disadvantages:
# - May be overlooked by developers who are not familiar with the format.
# Suitable use cases:
# - Ideal for documenting functions, classes, and modules in Python.
# (b) Inline comments:
# Advantages:
# - Provides immediate context and explanations for specific lines of code.
# Disadvantages:
# - Can clutter the code if overused, making it harder to read.
# Suitable use cases:
# - Best for explaining complex logic or specific implementation details within the code.
# (c) Google-style documentation:
# Advantages:
# - Provides a clear and consistent format for documenting code, making it easier to read and understand.
# Disadvantages:
# - May require more effort to maintain and update compared to inline comments.
# Suitable use cases:
# - Ideal for larger projects or libraries where consistent documentation is crucial for maintainability.
# 3. Recommendation:
# For new developers onboarding a project, the Google-style documentation would be most helpful. This is
# because it provides a clear and consistent format that is widely recognized and supported by tools like Sphinx, making it easier for new developers to understand the function's purpose, parameters, and return values. Additionally, the structured format can help new developers quickly grasp the functionality of the code without needing to read through inline comments or decipher less formal docstrings.


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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

#Task 4:
#generate a pydoc documentation in conversion.py with functions:o decimal_to_binary(n)o binary_to_decimal(b) o decimal_to_hexadecimal(n).
def decimal_to_binary(n):
    """
    Converts a decimal number to its binary representation.

    Parameters:
    n (int): The decimal number to be converted.

    Returns:
    str: The binary representation of the input decimal number.
    """
    return bin(n)[2:]  # Remove the '0b' prefix
def binary_to_decimal(b):
    """
    Converts a binary number (as a string) to its decimal representation.
    Parameters: 
    b (str): The binary number to be converted, represented as a string.
    Returns:
    int: The decimal representation of the input binary number.
    """
    return int(b, 2)  # Convert binary string to decimal integer
def decimal_to_hexadecimal(n):
    """
    Converts a decimal number to its hexadecimal representation.

    Parameters:
    n (int): The decimal number to be converted.

    Returns:
    str: The hexadecimal representation of the input decimal number.
    """
    return hex(n)[2:]  # Remove the '0x' prefix

#Task 5:
#generate a pydoc documentation in  course.py with functions:add_course(course_id, name, credits), remove_course(course_id) and get_course(course_id).
def add_course(course_id, name, credits):
    """
    Adds a course to the course catalog.

    Parameters:
    course_id (str): The unique identifier for the course.
    name (str): The name of the course.
    credits (int): The number of credits for the course.

    Returns:
    dict: A dictionary representing the added course.
    """
    return {"course_id": course_id, "name": name, "credits": credits}
def remove_course(course_id):
    """
    Removes a course from the course catalog.

    Parameters:
    course_id (str): The unique identifier for the course to be removed.

    Returns:
    str: A message indicating whether the course was successfully removed or not found.
    """
    # This is a placeholder implementation. In a real application, you would check if the course exists and remove it from a database or data structure.
    return f"Course with ID {course_id} has been removed."
def get_course(course_id):
    """
    Retrieves a course from the course catalog.
    Parameters:
    course_id (str): The unique identifier for the course to be retrieved.
    Returns:
    dict: A dictionary representing the course details if found, or a message indicating that the course was not found.
    """
    # This is a placeholder implementation. In a real application, you would look up the course in a database or data structure.
    return {"course_id": course_id, "name": "Sample Course", "credits": 3}


