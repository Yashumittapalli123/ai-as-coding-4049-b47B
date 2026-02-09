#Task 1:
'''
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
print(add_item(1))
print(add_item(2, []))

#Task 2:
import math

def check_sum():
    return math.isclose(0.1 + 0.2, 0.3)
print(check_sum())

#Task 3:
def countdown(n):
    if n <= 0:
        return
    print(n)
    return countdown(n-1)
countdown(5)

#Task 4:
def get_value():
    data = {"a": 1, "b": 2}
    return data.get("c")
print(get_value())

#Task 5:
def loop_example():
    i = 0
    while i < 5:
        print(i)
        i += 1   # Increment i so the loop can end
loop_example()

#Task 6:
#fix the bug in the following code snippet and explain the issue:
#The issue was incorrect unpacking syntax. The tuple (1, 2, 3) has 3 elements 
#and we need exactly 3 variables on the left side to unpack it.
a, b, c = 1, 2, 3
print(a, b, c)

#Task 7:
#fix the bug in the following code snippet and explain the issue:

def func():
    x = 5
    y = 10
    return x+y

#Task 8:
import math
print(math.sqrt(16))

#Task 9:
def total(numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum
print(total([1,2,3]))

#Task 10:
def calculate_area(length, width):
    return length * width
print(calculate_area(5, 10))

#Task 11:
#fix the bug in the following code snippet and explain the issue:
def add_values():
    return 5 + int("10")
print(add_values()) 
# The issue was that the string "10" needed to be converted to an integer before addition.

#Task 12:
#fix the bug in the following code snippet and explain the issue:
def combine():
    numbers = [1, 2, 3]
    return "Numbers: " + str(numbers)
print(combine())
# The issue was that we were trying to concatenate a list directly to a string, which is not allowed. We needed to convert the list to a string first using str().
'''
#TASK 13:
#fix the bug in the following code snippet and explain the issue:
'''def repeat_text():
    return "Hello" * 2.5
print(repeat_text())'''
# The issue was that multiplying a string by a float (2.5) is not allowed in Python. We needed to use an integer to specify the number of repetitions. Changing 2.5 to
# 2 fixes the issue.
'''
def repeat_text():
    return "Hello" * 2  
print(repeat_text())
# The corrected code now successfully repeats the string "Hello" two times, resulting in "HelloHello".
'''
#Task 14:
#fix the bug in the following code snippet and explain the issue:
'''
def compute():
    value = None
    return value + 10

print(compute())
# The issue was that we were trying to add an integer (10) to a NoneType (value), which is not allowed. We needed to initialize value with a number before performing the addition.
def compute():
    value = 0  # Initialize value to a number
    return value + 10
print(compute())'''
# The corrected code now successfully adds 10 to the initialized value (0), resulting in 10.

#Task 15:
#fix the bug in the following code snippet and explain the issue:
'''
def sum_two_numbers():
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    return a + b

print(sum_two_numbers())'''
# The issue was that the input function returns a string, so we were concatenating two strings instead of adding two numbers. We needed to convert the inputs to integers before performing the addition.
def sum_two_numbers():
    a = int(input("Enter first number: "))  # Convert input to integer
    b = int(input("Enter second number: "))  # Convert input to integer
    return a + b
print(sum_two_numbers())
# The corrected code now successfully converts the user inputs to integers before adding them, resulting in the correct sum of the two numbers.











