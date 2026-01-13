
# # Task 1
# '''
# Prompt :
# You are an AI coding assistant.
# Write a Python function in Google Colab that:
# Accepts a list of numbers as input
# Calculates the mean, minimum, and maximum values
# Prints the results clearly

# Then run the function on the list [12, 7, 9, 21, 5] and show the output.
# '''

# def calculate_statistics(numbers):
#     if not numbers:
#         print("List is empty")
#         return

#     mean_value = sum(numbers) / len(numbers)
#     min_value = min(numbers)
#     max_value = max(numbers)

#     print("Mean:", mean_value)
#     print("Minimum:", min_value)
#     print("Maximum:", max_value)

# test_list = [12, 7, 9, 21, 5]
# calculate_statistics(test_list)


# # Task 2
# '''
# Prompt: Armstrong Number Checker
# Write a Python function that checks if a number is an Armstrong number.
# Test it with 153 and 123, and print the results clearly.
# '''

# def is_armstrong_number(number):
#     num_str = str(number)
#     power = len(num_str)
#     total = sum(int(digit) ** power for digit in num_str)
#     return total == number

# for num in [153, 123]:
#     if is_armstrong_number(num):
#         print(f"{num} is an Armstrong number")
#     else:
#         print(f"{num} is not an Armstrong number")


# # Task 3
# '''
# Prompt:
# Write a Python function is_leap_year(year) that returns True if the year is a leap year, otherwise False.
# Test it with 2000, 2021, 2024, and 2100.
# '''

# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             return year % 400 == 0
#         return True
#     return False

# for year in [2000, 2021, 2024, 2100]:
#     if is_leap_year(year):
#         print(f"{year} is a leap year")
#     else:
#         print(f"{year} is not a leap year")


# # Task 4: Student Logic + AI Refactoring (Odd/Even Sum)
# '''
# Company policy requires developers to write logic before using AI.
# Write a Python program that calculates the sum of odd and even numbers in a tuple,
# then refactor it using AI.
# '''

# Original code 
def calculate_sums_original(numbers):
    even_sum = 0
    odd_sum = 0

    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

    return even_sum, odd_sum

# Refactored code (AI Version)
def calculate_sums_refactored(numbers):
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    return even_sum, odd_sum

test_tuple = (1, 2, 3, 4, 5, 6)

print("Original Code Output:")
even_sum, odd_sum = calculate_sums_original(test_tuple)
print("Even sum:", even_sum)
print("Odd sum:", odd_sum)

print("\nRefactored Code Output:")
even_sum, odd_sum = calculate_sums_refactored(test_tuple)
print("Even sum:", even_sum)
print("Odd sum:", odd_sum)
