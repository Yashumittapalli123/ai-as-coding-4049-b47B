#TASK 1:

#generate a python program that accepts year as input and checks whether it is a leap year or not.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")  

#TASK 2:

#generate a python program that converts centimeters to inches like 10cm = 3.93701 inches
cm = float(input("Enter length in centimeters: "))
inches = cm / 2.54
print(f"{cm} cm = {inches} inches")

#TASK 3:

#write a python program that accepts a full name and formats it as "Last Name, First Name" like "John Smith" to "Smith, John" and "Anitha Rao" to "Rao, Anitha".
full_name = input("Enter your full name: ")
first_name, last_name = full_name.split() 
formatted_name = f"{last_name}, {first_name}"
print("Formatted name:", formatted_name)

#TASK 4:
#generate a python code that reads a string and that code should contain a function that counts vowels in a string using zero-shot prompting,few-shot prompting 
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in input_string if char in vowels)
    return count
input_string = input("Enter a string: ")
vowel_count = count_vowels(input_string)
print(f"The number of vowels in the string is: {vowel_count}")

def count_vowels_zero_shot(input_string):
    """
    Counts the number of vowels in a given string using zero-shot prompting.
    
    Args:
        input_string (str): The string to analyze
        
    Returns:
        int: The count of vowels in the string
    """
    vowels = "aeiouAEIOU"
    count = sum(1 for char in input_string if char in vowels)
    return count
count=count_vowels_zero_shot("Hello World")
print(f"Number of vowels (Zero-shot): {count}")
def count_vowels_few_shot(input_string):
    """
    Counts the number of vowels in a given string using few-shot prompting.
    
    Args:
        input_string (str): The string to analyze
        
    Returns:
        int: The count of vowels in the string
    """
    examples = [
        ("Hello", 2),
        ("World", 1),
        ("Python Programming", 4),
        ("OpenAI", 3)
    ]
    
    vowels = "aeiouAEIOU"
    count = sum(1 for char in input_string if char in vowels)
    return count
count=count_vowels_few_shot("Hello World")
print(f"Number of vowels (Few-shot): {count}")      
# Comparison Table                          
comparison_table = """
| Criteria        | Zero-shot Prompting               | Few-shot Prompting                |
|-----------------|-----------------------------------|-----------------------------------|
| Accuracy        | High                              | High                              |
| Readability     | Clear and concise                 | Slightly more verbose             |
| Logical Clarity | Direct and straightforward        | Demonstrates examples for clarity |
"""     
print(comparison_table)
#Logic : The function count_vowels counts the number of vowels in a given string. The zero-shot and few-shot prompting functions demonstrate different approaches to achieve the same result.

#Task-5
#generate a python code that reads a text file and counts the number of lines in it and prints the count
def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
            return line_count
    except FileNotFoundError:
        return "File not found. Please check the file path."
file_path = input("Enter the path of the text file: ")
line_count = count_lines_in_file(file_path)
print(f"The number of lines in the file is: {line_count}")
#Logic : The function count_lines_in_file reads a text file and counts the number of lines in it, handling the case where the file may not be found.
