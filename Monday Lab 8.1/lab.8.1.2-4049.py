# ============================================================
# Lab 8.1.1 — Testing Tasks (assert / unittest / pytest)
# ============================================================

import re
import unittest
import string
from datetime import datetime

# Task 1 — Strong Password Validator

def is_strong_password(password: str) -> bool:
    """Return True if password meets all strength requirements."""
    if not isinstance(password, str) or len(password) < 8:
        return False
    if " " in password:
        return False
    return all([
        re.search(r"[A-Z]", password),
        re.search(r"[a-z]", password),
        re.search(r"\d",    password),
        re.search(r"[^\w]", password),
    ])


# Assert tests
assert is_strong_password("Abcd@123")       == True
assert is_strong_password("abcd123")        == False
assert is_strong_password("ABCdef12!")      == True
assert is_strong_password("StrongPass1!")   == True
assert is_strong_password("weakpass1")      == False
assert is_strong_password("NoSpecialChar1") == False
assert is_strong_password("Valid Pass1@")   == False   # space
assert is_strong_password("A1@a")           == False   # too short

print("Task 1 — assert tests passed")


class TestPassword(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(is_strong_password("ValidPass1@"))

    def test_no_upper(self):
        self.assertFalse(is_strong_password("validpass1@"))

    def test_has_space(self):
        self.assertFalse(is_strong_password("Valid Pass1@"))

    def test_no_special(self):
        self.assertFalse(is_strong_password("ValidPass12"))

    def test_no_digit(self):
        self.assertFalse(is_strong_password("ValidPass@@"))


# pytest-compatible tests
def test_pw_valid():
    assert is_strong_password("Another1@") is True

def test_pw_short():
    assert is_strong_password("A1@a") is False

def test_pw_no_digit():
    assert is_strong_password("NoDigit@@") is False


# Task 2 — Number Classifier


def classify_number(n):
    """Return 'Positive', 'Negative', 'Zero', or 'Invalid'."""
    if not isinstance(n, (int, float)) or isinstance(n, bool):
        return "Invalid"
    if n == 0:
        return "Zero"
    return "Positive" if n > 0 else "Negative"


# Assert tests
assert classify_number(10)    == "Positive"
assert classify_number(-5)    == "Negative"
assert classify_number(0)     == "Zero"
assert classify_number(1)     == "Positive"
assert classify_number(-1)    == "Negative"
assert classify_number("abc") == "Invalid"
assert classify_number(None)  == "Invalid"
assert classify_number([])    == "Invalid"
assert classify_number({})    == "Invalid"

print("Task 2 — assert tests passed")


class TestNumber(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(classify_number(4), "Positive")

    def test_negative(self):
        self.assertEqual(classify_number(-2), "Negative")

    def test_zero(self):
        self.assertEqual(classify_number(0), "Zero")

    def test_invalid_list(self):
        self.assertEqual(classify_number([]), "Invalid")

    def test_invalid_bool(self):
        self.assertEqual(classify_number(True), "Invalid")


# pytest-compatible tests
def test_num_positive():
    assert classify_number(3) == "Positive"

def test_num_negative():
    assert classify_number(-3) == "Negative"

def test_num_invalid():
    assert classify_number({}) == "Invalid"


# Task 3 — Anagram Checker


def is_anagram(str1, str2) -> bool:
    """Return True if str1 and str2 are anagrams (ignoring case, spaces, punctuation)."""
    if not isinstance(str1, str) or not isinstance(str2, str):
        return False

    def clean(s):
        return sorted(ch.lower() for ch in s if ch.isalnum())

    return clean(str1) == clean(str2)


# Assert tests
assert is_anagram("listen",     "silent")       == True
assert is_anagram("hello",      "world")         == False
assert is_anagram("Dormitory",  "Dirty Room")    == True
assert is_anagram("",           "")              == True
assert is_anagram("Same",       "Same")          == True
assert is_anagram("Astronomer", "Moon starer")   == True
assert is_anagram(None,         "silent")        == False

print("Task 3 — assert tests passed")


class TestAnagram(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_anagram("Triangle", "Integral"))

    def test_false(self):
        self.assertFalse(is_anagram("Apple", "Pabble"))

    def test_empty(self):
        self.assertTrue(is_anagram("", ""))

    def test_case_space(self):
        self.assertTrue(is_anagram("School master", "The classroom"))

    def test_none_input(self):
        self.assertFalse(is_anagram(None, "silent"))


# pytest-compatible tests
def test_ana_true():
    assert is_anagram("Debit Card", "Bad Credit") is True

def test_ana_false():
    assert is_anagram("Test", "Best") is False

def test_ana_identical():
    assert is_anagram("Python", "Python") is True


# Task 4 — Inventory Manager

class Inventory:
    """Simple stock management system."""

    def __init__(self):
        self.stock: dict = {}

    def add_item(self, name: str, quantity: int) -> None:
        if quantity <= 0:
            return
        self.stock[name] = self.stock.get(name, 0) + quantity

    def remove_item(self, name: str, quantity: int) -> None:
        if name not in self.stock or quantity <= 0:
            return
        self.stock[name] = max(0, self.stock[name] - quantity)

    def get_stock(self, name: str) -> int:
        return self.stock.get(name, 0)


# Assert tests
inv = Inventory()
inv.add_item("Pen", 10)
assert inv.get_stock("Pen") == 10

inv.remove_item("Pen", 5)
assert inv.get_stock("Pen") == 5

inv.add_item("Book", 3)
assert inv.get_stock("Book") == 3

inv.remove_item("Pen", 20)          # remove beyond stock → clamp to 0
assert inv.get_stock("Pen") == 0

assert inv.get_stock("Pencil") == 0  # item never added

print("Task 4 — assert tests passed")


class TestInventory(unittest.TestCase):
    def test_add(self):
        i = Inventory()
        i.add_item("Notebook", 4)
        self.assertEqual(i.get_stock("Notebook"), 4)

    def test_remove(self):
        i = Inventory()
        i.add_item("Marker", 6)
        i.remove_item("Marker", 2)
        self.assertEqual(i.get_stock("Marker"), 4)

    def test_remove_overflow(self):
        i = Inventory()
        i.add_item("Eraser", 2)
        i.remove_item("Eraser", 5)
        self.assertEqual(i.get_stock("Eraser"), 0)

    def test_missing_item(self):
        i = Inventory()
        self.assertEqual(i.get_stock("Unknown"), 0)

    def test_add_zero(self):
        i = Inventory()
        i.add_item("Ghost", 0)
        self.assertEqual(i.get_stock("Ghost"), 0)


# pytest-compatible tests
def test_inv_add():
    i = Inventory()
    i.add_item("Bag", 1)
    assert i.get_stock("Bag") == 1

def test_inv_remove():
    i = Inventory()
    i.add_item("Bag", 5)
    i.remove_item("Bag", 3)
    assert i.get_stock("Bag") == 2

def test_inv_missing():
    i = Inventory()
    assert i.get_stock("Nothing") == 0

# Task 5 — Date Validator & Formatter


def validate_and_format_date(date_str) -> str:
    """Parse MM/DD/YYYY and return YYYY-MM-DD, or 'Invalid Date'."""
    if not isinstance(date_str, str):
        return "Invalid Date"
    try:
        d = datetime.strptime(date_str, "%m/%d/%Y")
        return d.strftime("%Y-%m-%d")
    except ValueError:
        return "Invalid Date"


# Assert tests
assert validate_and_format_date("10/15/2023") == "2023-10-15"
assert validate_and_format_date("02/30/2023") == "Invalid Date"
assert validate_and_format_date("01/01/2024") == "2024-01-01"
assert validate_and_format_date("13/01/2024") == "Invalid Date"   # invalid month
assert validate_and_format_date("abc")         == "Invalid Date"
assert validate_and_format_date(None)          == "Invalid Date"
assert validate_and_format_date(12345)         == "Invalid Date"

print("Task 5 — assert tests passed")


class TestDate(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_and_format_date("12/25/2022"), "2022-12-25")

    def test_invalid_day(self):
        self.assertEqual(validate_and_format_date("02/31/2022"), "Invalid Date")

    def test_invalid_format(self):
        self.assertEqual(validate_and_format_date("2022-12-25"), "Invalid Date")

    def test_non_string(self):
        self.assertEqual(validate_and_format_date(99), "Invalid Date")

    def test_invalid_month(self):
        self.assertEqual(validate_and_format_date("00/10/2020"), "Invalid Date")


# pytest-compatible tests
def test_date_valid():
    assert validate_and_format_date("07/04/2020") == "2020-07-04"

def test_date_invalid():
    assert validate_and_format_date("00/10/2020") == "Invalid Date"

def test_date_type():
    assert validate_and_format_date(12345) == "Invalid Date"


# ──────────────────────────────────────────────
# Run all unittest suites
# ──────────────────────────────────────────────
if __name__ == "__main__":
    unittest.main()
