#TASK 1:Generate code to fetch weather data securely without exposing API keys in the code.
'''
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        return f"Weather in {city}: {weather}, Temperature: {temperature}°C"
    else:
        return f"API Error {response.status_code}: {data.get('message', data)}"


if __name__ == "__main__":
    city = input("Enter city name: ")
    print(get_weather(city))


#Task 2:
#Generate a Python script that stores user details (name, email, password) in a file. Then analyze if storing the password is secure and modify the script to store the password safely using hashing instead of plain text.
import os
import hashlib
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def store_user_details(name, email, password):
    hashed_password = hash_password(password)
    with open("user_details.txt", "a") as file:
        file.write(f"Name: {name}, Email: {email}, Password: {hashed_password}\n")
if __name__ == "__main__":
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    store_user_details(name, email, password)
    print("User details stored securely.")
# Storing passwords in plain text is insecure as it exposes sensitive information to anyone who has access to the file.
# Hashing the password before storing it enhances security by ensuring that the actual password is not saved directly.

#TASK 3:
#generate an Armstrong number checking function with comments and explanations and explain the code line by line ,compare the explanation with full code functionality.
def is_armstrong_number(num):
    """
    This function checks if a number is an Armstrong number.
    An Armstrong number for a given number of digits is an integer such that the sum of its own digits each raised to the power of the number of digits is equal to the number itself.
    For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.
    """
    # Convert the number to string to easily iterate over each digit
    str_num = str(num)
    # Get the number of digits in the number
    num_digits = len(str_num)
    # Initialize a variable to hold the sum of the digits raised to the power of num_digits
    sum_of_powers = 0
    
    # Iterate over each digit in the string representation of the number
    for digit in str_num:
        # Convert the digit back to integer and raise it to the power of num_digits, then add it to sum_of_powers
        sum_of_powers += int(digit) ** num_digits
    
    # Check if the calculated sum_of_powers is equal to the original number
    return sum_of_powers == num
# Example usage
number = int(input("Enter a number to check if it's an Armstrong number: "))
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
# Explanation of the code:
# 1. The function `is_armstrong_number` takes an integer `num` as input.
# 2. It converts the number to a string to facilitate iteration over each digit.
# 3. It calculates the number of digits in the number.
# 4. It initializes a variable `sum_of_powers` to store the cumulative sum of each digit raised to the power of the number of digits.
# 5. It iterates over each digit, converts it back to an integer, raises it to the power of `num_digits`, and adds it to `sum_of_powers`.
# 6. Finally, it checks if `sum_of_powers` is equal to the original number and returns True if they are equal (indicating that it is an Armstrong number) or False otherwise.
# The functionality of the code matches the explanation provided, as it correctly identifies Armstrong numbers based on the defined criteria.


#TASK 4:
#Generate Python code for QuickSort and BubbleSort, and include comments explaining step-by-step how each works and where they differ.
def quicksort(arr):
    """
    QuickSort is a divide-and-conquer algorithm that sorts an array by selecting a 'pivot' element
    and partitioning the other elements into two sub-arrays according to whether they are less than or greater than the pivot.
    The sub-arrays are then sorted recursively.
    """
    if len(arr) <= 1:
        return arr  # Base case: arrays with 0 or 1 element are already sorted
    else:
        pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
        left = [x for x in arr if x < pivot]  # Elements less than the pivot
        middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
        right = [x for x in arr if x > pivot]  # Elements greater than the pivot
        return quicksort(left) + middle + quicksort(right)  # Recursively sort and combine the sub-arrays
        
def bubblesort(arr):
    """
    BubbleSort is a simple sorting algorithm that repeatedly steps through the list,
    compares adjacent elements and swaps them if they are in the wrong order.
    The process is repeated until the list is sorted.
    """
    n = len(arr)
    for i in range(n):
        # Track if a swap was made; if no swaps occur, the array is sorted
        swapped = False
        for j in range(0, n-i-1):  # Last i elements are already sorted
            if arr[j] > arr[j+1]:  # Compare adjacent elements
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap if they are in the wrong order
                swapped = True
        if not swapped:
            break  # If no swaps were made, the array is sorted
    return arr
if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers separated by space: ").split()))

    print("Original array:", arr)
    print("QuickSort result:", quicksort(arr))
    print("BubbleSort result:", bubblesort(arr.copy()))

'''
#TASK 5:
#Generate a recommendation system that also provides reasons for each suggestion.
import random
def recommend_items(user_preferences, items):
    recommendations = []
    for item in items:
        score = 0
        reasons = []
        for preference in user_preferences:
            if preference in item['tags']:
                score += 1
                reasons.append(f"Matches your preference for {preference}")
        if score > 0:
            recommendations.append((item['name'], score, reasons))
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations
if __name__ == "__main__":
    user_preferences = ['action', 'comedy', 'drama']
    items = [
        {'name': 'Movie A', 'tags': ['action', 'thriller']},
        {'name': 'Movie B', 'tags': ['comedy', 'romance']},
        {'name': 'Movie C', 'tags': ['drama', 'biography']},
        {'name': 'Movie D', 'tags': ['horror', 'thriller']},
    ]
    recommendations = recommend_items(user_preferences, items)
    for name, score, reasons in recommendations:
        print(f"Recommended: {name} (Score: {score})")
        for reason in reasons:
            print(f" - {reason}")


