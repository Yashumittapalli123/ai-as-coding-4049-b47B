#Task1

import re

def is_strong_password(password):
    """
    Checks if a password meets strong security criteria:
    - At least 8 characters long
    - Contains no spaces
    - Has at least one uppercase letter
    - Has at least one lowercase letter
    - Has at least one digit
    - Has at least one special character (non-alphanumeric)
    """
    if len(password) < 8 or " " in password:
        return False

    # Check for required character types using regex
    # The regex checks for at least one occurrence of:
    # [A-Z] : Uppercase
    # [a-z] : Lowercase
    # [0-9] : Digit
    # [^\w] : Special character (anything not a word character)
    # Note: \w includes [a-zA-Z0-9_], so underscore is considered a word character here.
    patterns = [r"[A-Z]", r"[a-z]", r"\d", r"[^\w]"]
    
    return all(re.search(p, password) for p in patterns)
# Test cases
assert is_strong_password("Abcd@123") == True
assert is_strong_password("abcd123") == False
assert is_strong_password("ABcd1234") == False   # no special char
assert is_strong_password("ABCD@1234") == False  # no lowercase
assert is_strong_password("Abc d@123") == False  # contains space
print("Task 1: All tests passed.")




#Task2
def classify_number(n):
    """
    Classifies a number as Positive, Negative, or Zero.
    Returns 'Invalid Input' for non-numeric types.
    """
    if not isinstance(n, (int, float)):
        return "Invalid Input"

    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

# Test cases
assert classify_number(10) == "Positive"
assert classify_number(-5) == "Negative"
assert classify_number(0) == "Zero"
assert classify_number(1) == "Positive"
assert classify_number(-1) == "Negative"
assert classify_number("abc") == "Invalid Input"
assert classify_number(None) == "Invalid Input"
print("Task 2: All tests passed.")


#Task3
from collections import Counter

def is_anagram(str1, str2):
    """
    Checks if two strings are anagrams, ignoring case, spaces, and punctuation.
    Uses Counter for O(n) complexity.
    """
    def clean_counter(s):
        # Generator expression to filter and normalize characters
        return Counter(ch.lower() for ch in s if ch.isalnum())

    return clean_counter(str1) == clean_counter(str2)

# Test cases
assert is_anagram("listen", "silent") == True
assert is_anagram("hello", "world") == False
assert is_anagram("Dormitory", "Dirty Room") == True
assert is_anagram("", "") == True                 # empty strings
assert is_anagram("Tea", "Eat") == True           # case-insensitive
assert is_anagram("A gentleman!", "Elegant man") == True  # punctuation ignored

print("Task 3: All tests passed.")


#Task4
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        """Adds quantity to an item. Ignores non-positive quantities."""
        if quantity > 0:
            self.items[name] = self.items.get(name, 0) + quantity

    def remove_item(self, name, quantity):
        """Removes quantity from an item. Ensures stock doesn't go below zero."""
        if name in self.items and quantity > 0:
            current_stock = self.items[name]
            # Use max to ensure stock doesn't drop below zero
            self.items[name] = max(0, current_stock - quantity)

    def get_stock(self, name):
        """Returns the current stock of an item, defaulting to 0."""
        return self.items.get(name, 0)

inv = Inventory()

# Test cases
inv.add_item("Pen", 10)
assert inv.get_stock("Pen") == 10

inv.remove_item("Pen", 5)
assert inv.get_stock("Pen") == 5

inv.add_item("Book", 3)
assert inv.get_stock("Book") == 3

inv.remove_item("Pen", 10)     # removing more than available
assert inv.get_stock("Pen") == 0

assert inv.get_stock("Pencil") == 0   # item not added yet

print("Task 4: All tests passed.")


#Task5
from datetime import datetime

def validate_and_format_date(date_str):
    """
    Parses a date string in MM/DD/YYYY format and returns it in YYYY-MM-DD format.
    Returns 'Invalid Date' if parsing fails.
    """
    try:
        dt = datetime.strptime(date_str, "%m/%d/%Y")
        return dt.strftime("%Y-%m-%d")
    except ValueError:
        return "Invalid Date"

# Test cases
assert validate_and_format_date("10/15/2023") == "2023-10-15"
# Note: "02/30/2023" is invalid because Feb never has 30 days
assert validate_and_format_date("02/30/2023") == "Invalid Date"
assert validate_and_format_date("01/01/2024") == "2024-01-01"
assert validate_and_format_date("13/01/2023") == "Invalid Date"   # invalid month
assert validate_and_format_date("abc") == "Invalid Date"          # wrong format
assert validate_and_format_date("02/29/2024") == "2024-02-29"     # leap year valid
print("Task 5: All tests passed.")
