# Task-1
# Write a program to manage student records with Name, Roll Number, and CGPA. Implement Quick Sort and Merge Sort to sort students in descending order of CGPA. Include functionality to measure and compare execution time for both algorithms on large datasets. Also, display the top 10 students with highest CGPA.
from heapq import merge
import time
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __str__(self):
        return f"{self.name} (Roll No: {self.roll_number}, CGPA: {self.cgpa})"
def quick_sort(students):
    if len(students) <= 1:
        return students
    pivot = students[len(students) // 2].cgpa
    left = [x for x in students if x.cgpa > pivot]
    middle = [x for x in students if x.cgpa == pivot]
    right = [x for x in students if x.cgpa < pivot]
    return quick_sort(left) + middle + quick_sort(right)
def merge_sort(students):
    if len(students) <= 1:
        return students
    mid = len(students) // 2
    left_half = merge_sort(students[:mid])
    right_half = merge_sort(students[mid:])
    return merge(left_half, right_half)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i].cgpa > right[j].cgpa:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
def main():
    students = [
        Student("Alice", 1, 3.8),
        Student("Bob", 2, 3.5),
        Student("Charlie", 3, 3.9),
        Student("David", 4, 3.6),
        Student("Eve", 5, 3.7),
        Student("Frank", 6, 3.4),
        Student("Grace", 7, 3.9),
        Student("Heidi", 8, 3.2),
        Student("Ivan", 9, 3.8),
        Student("Judy", 10, 3.5)
    ]
    # Measure execution time for Quick Sort
    start_time = time.time()
    sorted_students_quick = quick_sort(students)
    end_time = time.time()
    print(f"Quick Sort Execution Time: {end_time - start_time:.6f} seconds")
    # Measure execution time for Merge Sort
    start_time = time.time()
    sorted_students_merge = merge_sort(students)
    end_time = time.time()
    print(f"Merge Sort Execution Time: {end_time - start_time:.6f} seconds")
    # Display top 10 students with highest CGPA
    print("\nTop 10 Students with Highest CGPA:")
    for student in sorted_students_quick[:10]:
        print(student)
if __name__ == "__main__":
    main()

# Task-2
# Write a Python program to implement Bubble Sort. Add detailed inline comments explaining each step, including comparisons, swapping of elements, passes through the list, and termination condition. Also include a clear time complexity analysis for best, average, and worst cases.
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Initialize a flag to check if any swapping occurs
        swapped = False
        # Last i elements are already in place, no need to check them
        for j in range(0, n - i - 1):
            # Compare the adjacent elements
            if arr[j] > arr[j + 1]:
                # If the element found is greater than the next element, swap them
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swapping occurred, the list is already sorted, so we can break out of the loop
        if not swapped:
            break
    return arr
# Time Complexity Analysis:
# Best Case: O(n) - This occurs when the input list is already sorted. The algorithm makes one pass through the
# list to check if it is sorted, and since no swaps are needed, it terminates early.
# Average Case: O(n^2) - This occurs when the input list is in random order. The algorithm will need to make multiple passes through the list, and in each pass, it may need to compare and swap elements.
# Worst Case: O(n^2) - This occurs when the input list is sorted in reverse order. The algorithm will need to make n-1 passes through the list, and in each pass, it will need to compare and swap elements, resulting in n*(n-1)/2 comparisons and swaps.
# Example usage
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    sorted_arr = bubble_sort(arr)
    print("Sorted array:", sorted_arr)
    
# Task-3
# Given partially implemented recursive functions for Quick Sort and Merge Sort in Python, complete the missing logic for both algorithms. Add meaningful docstrings explaining the recursion process. Then write code to test and compare their performance on random, sorted, and reverse-sorted lists. Finally, include a clear explanation of best, average, and worst-case time complexities for both algorithms.
import random
def quick_sort(arr):
    """
    Quick Sort is a divide-and-conquer algorithm that sorts an array by selecting a 'pivot' element and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

    The recursion process involves:
    1. Choosing a pivot element from the array.
    2. Partitioning the array into two sub-arrays: one with elements less than the pivot and one with elements greater than the pivot.
    3. Recursively applying the same process to the sub-arrays until they are sorted.

    Time Complexity:
    - Best Case: O(n log n) - This occurs when the pivot divides the array into two equal halves consistently.
    - Average Case: O(n log n) - This occurs when the pivots are reasonably well-chosen, leading to balanced partitions.
    - Worst Case: O(n^2) - This occurs when the smallest or largest element is always chosen as the pivot, leading to unbalanced partitions (e.g., when the array is already sorted or reverse-sorted).
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
def merge_sort(arr):
    """Merge Sort is a divide-and-conquer algorithm that sorts an array by recursively dividing it into two halves, sorting each half, and then merging the sorted halves back together. The recursion process involves:
    1. Dividing the array into two halves.
    2. Recursively sorting each half.
    3. Merging the sorted halves back together.

    Time Complexity:
    - Best Case: O(n log n) - This occurs when the array is divided into two equal halves at each step.
    - Average Case: O(n log n) - This occurs when the array is divided into two halves of roughly equal size at each step.
    - Worst Case: O(n log n) - This occurs when the array is divided into two halves of very different sizes at each step.
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
# Testing and comparing performance
if __name__ == "__main__":
    # Generate random, sorted, and reverse-sorted lists
    random_list = [random.randint(1, 100) for _ in range(1000)]
    sorted_list = sorted(random_list)
    reverse_sorted_list = sorted(random_list, reverse=True)

    # Test Quick Sort
    print("Testing Quick Sort...")
    print("Random List:", quick_sort(random_list.copy()))
    print("Sorted List:", quick_sort(sorted_list.copy()))
    print("Reverse Sorted List:", quick_sort(reverse_sorted_list.copy()))

    # Test Merge Sort
    print("\nTesting Merge Sort...")
    print("Random List:", merge_sort(random_list.copy()))
    print("Sorted List:", merge_sort(sorted_list.copy()))
    print("Reverse Sorted List:", merge_sort(reverse_sorted_list.copy()))
# #Task-4
# # Design a Python-based inventory management system for a retail store with product attributes: product ID, name, price, and stock quantity. Suggest and implement efficient search algorithms for finding products by ID and name, and sorting algorithms for organizing products by price and quantity. Choose appropriate algorithms based on large dataset size and frequent updates. Include a comparison table mapping each operation to the recommended algorithm with justification. Also provide working Python functions for searching and sorting the inventory
# class Product:
#     def __init__(self, product_id, name, price, stock_quantity):
#         self.product_id = product_id
#         self.name = name
#         self.price = price
#         self.stock_quantity = stock_quantity

#     def __str__(self):
#         return f"{self.name} (ID: {self.product_id}, Price: {self.price}, Stock: {self.stock_quantity})"
# class Inventory:
#     def __init__(self):
#         self.products = []

#     def add_product(self, product):
#         self.products.append(product)

#     def search_by_id(self, product_id):
#         """Search for a product by its ID using binary search. This is efficient for large datasets that are sorted by product ID."""
#         self.products.sort(key=lambda x: x.product_id)  # Ensure products are sorted by ID
#         left, right = 0, len(self.products) - 1
#         while left <= right:
#             mid = (left + right) // 2
#             if self.products[mid].product_id == product_id:
#                 return self.products[mid]
#             elif self.products[mid].product_id < product_id:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return None

#     def search_by_name(self, name):
#         """Search for a product by its name using linear search. This is suitable for small datasets or when the dataset is frequently updated."""
#         for product in self.products:
#             if product.name.lower() == name.lower():
#                 return product
#         return None

#     def sort_by_price(self):
#         """Sort products by price using Timsort (Python's built-in sorting algorithm), which is efficient for large datasets and partially sorted data."""
#         self.products.sort(key=lambda x: x.price)

#     def sort_by_stock_quantity(self):
#         """Sort products by stock quantity using Timsort, which is efficient for large datasets and partially sorted data."""
#         self.products.sort(key=lambda x: x.stock_quantity)
# # Comparison Table
# # | Operation           | Recommended Algorithm | Justification               |
# # |---------------------|-----------------------|-----------------------------|
# # | Search by ID        | Binary Search         | Efficient for sorted data   |
# # | Search by Name      | Linear Search         | Suitable for small datasets or frequent updates |
# # | Sort by Price       | Timsort (Python's built-in) | Efficient for large datasets and partially sorted data |
# # | Sort by Stock Quantity | Timsort (Python's built-in) | Efficient for large datasets and partially sorted data |
# # Example usage
# if __name__ == "__main__":
#     inventory = Inventory()
#     inventory.add_product(Product(1, "Laptop", 999.99, 10))
#     inventory.add_product(Product(2, "Smartphone", 499.99, 20))
#     inventory.add_product(Product(3, "Headphones", 199.99, 15))

#     # Search by ID
#     print("Search by ID (2):", inventory.search_by_id(2))

#     # Search by Name
#     print("Search by Name (Headphones):", inventory.search_by_name("Headphones"))

#     # Sort by Price
#     inventory.sort_by_price()
#     print("\nProducts sorted by price:")
#     for product in inventory.products:
#         print(product)

#     # Sort by Stock Quantity
#     inventory.sort_by_stock_quantity()
#     print("\nProducts sorted by stock quantity:")
#     for product in inventory.products:
#         print(product)
#Task-5  
# Write a Python program to simulate stock market data including stock symbol, opening price, and closing price, and calculate the percentage change for each stock. Implement Heap Sort manually (without using the heapq module) by defining custom heapify and heap_sort functions to sort the stocks in descending order based on percentage change. Implement an efficient search function using a Hash Map (dictionary) to quickly retrieve stock details by symbol, and also include a linear search for comparison. Measure and compare the execution time of Heap Sort with Python’s built-in sorted() function, and Hash Map search with linear search. Display the top gainers and losers, search results for a given stock symbol, and performance comparison outputs. Add clear comments explaining the logic for better understanding.
import random
import time
class Stock:
    def __init__(self, symbol, opening_price, closing_price):
        self.symbol = symbol
        self.opening_price = opening_price
        self.closing_price = closing_price

    def percentage_change(self):
        return ((self.closing_price - self.opening_price) / self.opening_price) * 100

    def __str__(self):
        return f"{self.symbol}: {self.percentage_change():.2f}%"
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left child index
    right = 2 * i + 2  # right child index

    # If left child is larger than root
    if left < n and arr[left].percentage_change() > arr[largest].percentage_change():
        largest = left

    # If right child is larger than largest so far
    if right < n and arr[right].percentage_change() > arr[largest].percentage_change():
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected sub-tree
def heap_sort(arr):
    n = len(arr)

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)
def hash_map_search(stock_dict, symbol):
    """Search for a stock by its symbol using a hash map (dictionary) for O(1) average time complexity."""
    return stock_dict.get(symbol, None)
def linear_search(stocks, symbol):
    """Search for a stock by its symbol using linear search with O(n) time complexity."""
    for stock in stocks:
        if stock.symbol == symbol:
            return stock
    return None
# Example usage
if __name__ == "__main__":
    # Simulate stock market data
    symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
    stocks = [Stock(symbol, random.uniform(100, 500), random.uniform(100, 500)) for symbol in symbols]

    # Create a hash map for quick search
    stock_dict = {stock.symbol: stock for stock in stocks}

    # Measure execution time for Heap Sort
    start_time = time.time()
    heap_sort(stocks)
    end_time = time.time()
    print(f"Heap Sort Execution Time: {end_time - start_time:.6f} seconds")

    # Measure execution time for built-in sorted() function
    start_time = time.time()
    sorted_stocks = sorted(stocks, key=lambda x: x.percentage_change(), reverse=True)
    end_time = time.time()
    print(f"Built-in sorted() Execution Time: {end_time - start_time:.6f} seconds")

    # Display top gainers and losers
    print("\nTop Gainers:")
    for stock in sorted_stocks[:3]:
        print(stock)

    print("\nTop Losers:")
    for stock in sorted_stocks[-3:]:
        print(stock)

    # Search for a given stock symbol
    search_symbol = 'AAPL'
    print(f"\nSearching for {search_symbol} using Hash Map:")
    result = hash_map_search(stock_dict, search_symbol)
    if result:
        print(result)
    else:
        print("Stock not found.")

    print(f"\nSearching for {search_symbol} using Linear Search:")
    result = linear_search(stocks, search_symbol)
    if result:
        print(result)
    else:
        print("Stock not found.")
