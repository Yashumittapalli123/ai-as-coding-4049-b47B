Task 5 – Real-Time Application: Algorithm Translation Across Languages

Scenario:
A company maintains algorithms written in different programming languages.
Examples:
• Converting a Python searching algorithm into C
• Translating a Java sorting program into JavaScript

Instructions:
• Use AI to translate a selected algorithm between two programming languages
• Execute and test both versions
• Document translation challenges such as:
  o Syntax differences
  o Library support
  o Memory management

Expected Output:
Equivalent, tested code implementations in two different programming languages.

Selected Algorithm: Bubble Sort
- From: Python
- To: JavaScript

Python Code (sort.py - from Task 3):
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr  # Added return for consistency

# Test
if __name__ == "__main__":
    test_list = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", test_list)
    bubble_sort(test_list)
    print("Sorted:", test_list)
```

JavaScript Code (sort.js):
```javascript
function bubbleSort(arr) {
    let n = arr.length;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
            }
        }
    }
    return arr;
}

// Test
let testArray = [64, 34, 25, 12, 22, 11, 90];
console.log("Original:", testArray);
let sortedArray = bubbleSort(testArray);
console.log("Sorted:", sortedArray);
```

Translation Challenges:
- Syntax differences: Python uses `range()` and `len()`, JavaScript uses `let` for variables, array `.length`, and destructuring assignment `[a, b] = [b, a]`
- Library support: Both are built-in, no external libraries needed
- Memory management: JavaScript handles memory automatically like Python; no manual allocation needed
- Execution: Python runs in interpreter, JavaScript needs Node.js runtime

Verification:
Both versions produce the same sorted output: [11, 12, 22, 25, 34, 64, 90]
