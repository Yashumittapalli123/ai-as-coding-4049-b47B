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
