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

