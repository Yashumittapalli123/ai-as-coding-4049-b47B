Task 3 – Pseudocode to Python Implementation

Task:
Translate a given pseudocode algorithm into Python using AI.

Instructions:
• Provide AI with pseudocode for sorting numbers (e.g., bubble sort or selection sort)
• Ask AI to convert it into executable Python code
• Validate correctness using sample input lists

Expected Output:
A working Python program that correctly implements the pseudocode logic.

Pseudocode (Bubble Sort):
```
procedure bubbleSort(A : list of sortable items)
    n = length(A)
    for i from 0 to n-1
        for j from 0 to n-i-1
            if A[j] > A[j+1]
                swap A[j] and A[j+1]
```

Python Code (sort.py):
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Test with sample input lists
if __name__ == "__main__":
    test_lists = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 1, 4, 2, 8],
        [3, 0, 2, 5, -1, 4, 1]
    ]
    for lst in test_lists:
        original = lst.copy()
        bubble_sort(lst)
        print(f"Original: {original} -> Sorted: {lst}")
```

Verification:
The Python implementation correctly sorts the lists in ascending order.
