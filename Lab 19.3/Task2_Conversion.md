Task 2 – Java to Python Function Conversion

Task:
Convert a Java method that checks whether a number is prime into Python.

Instructions:
• Ask AI to translate a Java isPrime() method into Python
• Test the function with multiple inputs
• Ensure the Python version follows Pythonic syntax and logic

Expected Output:
A correct Python function equivalent to the original Java prime-checking method.

Java Code:
```java
public static boolean isPrime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i <= Math.sqrt(n); i++) {
        if (n % i == 0) return false;
    }
    return true;
}
```

Python Code (prime.py):
```python
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Test the function with multiple inputs
if __name__ == "__main__":
    test_cases = [1, 2, 3, 4, 5, 17, 18, 19, 23, 24]
    for num in test_cases:
        print(f"{num} is prime: {is_prime(num)}")
```

Verification:
Running the Python code produces the expected prime checks.
