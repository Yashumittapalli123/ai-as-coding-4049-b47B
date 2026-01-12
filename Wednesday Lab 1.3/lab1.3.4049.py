#Task 1 fibonacci squence without function
# Ask the user for the number of terms
n = int(input("Enter the number of terms for Fibonacci sequence: "))

# Initialize the first two terms of the sequence
a = 0  # First term
b = 1  # Second term

# Print the Fibonacci sequence up to n terms
print("Fibonacci sequence:")
for i in range(n):
	print(a, end=" ")  # Print the current term
	c = a + b           # Calculate the next term
	a = b               # Update a to the next term
	b = c               # Update b to the next term

#Task 2 optimize fibonacci
# Ask the user for the number of terms
n = int(input("Enter the number of terms for Fibonacci sequence: "))

# Print the Fibonacci sequence up to n terms using minimal variables
print("Fibonacci sequence:")
fib1, fib2 = 0, 1  # Start with the first two terms
for i in range(n):
    print(fib1, end=" ")  # Print the current term
    # Update both variables in a single line, reducing temporary variables
    fib1, fib2 = fib2, fib1 + fib2


# Task 3: Modular Fibonacci Function
# This function generates the Fibonacci sequence up to n terms
def fibonacci_sequence(n):
	"""
	Returns a list containing the Fibonacci sequence up to n terms.
	Uses minimal variables and efficient loop logic.
	"""
	seq = []
	a, b = 0, 1  # Start with first two terms
	for _ in range(n):
		seq.append(a)  # Add current term to sequence
		a, b = b, a + b  # Update both variables in one line
	return seq

# Example usage: ask user and print sequence
if __name__ == "__main__":
	n = int(input("Enter the number of terms for Fibonacci sequence: "))
	print("Fibonacci sequence:")
	print(*fibonacci_sequence(n))



# Task 5: Iterative and Recursive Fibonacci Implementations

# Iterative Fibonacci (using loop)
def fibonacci_iterative(n):
	"""
	Returns Fibonacci sequence up to n terms using iteration.
	Step-by-step:
	1. Start with two variables (a, b).
	2. Loop n times, updating a and b.
	3. Append each term to the result list.
	"""
	seq = []
	a, b = 0, 1
	for _ in range(n):
		seq.append(a)
		a, b = b, a + b
	return seq

# Recursive Fibonacci (using function calls)
def fibonacci_recursive(n):
	"""
	Returns Fibonacci sequence up to n terms using recursion.
	Step-by-step:
	1. Base cases: return n if n==0 or n==1.
	2. Otherwise, call itself for (n-1) and (n-2).
	3. Used to build sequence by calling for each term.
	"""
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Build sequence using recursion
def fibonacci_sequence_recursive(n):
	return [fibonacci_recursive(i) for i in range(n)]

# Example usage and comparison
if __name__ == "__main__":
	n = int(input("Enter the number of terms for Fibonacci sequence: "))
	print("Iterative Fibonacci:")
	print(*fibonacci_iterative(n))
	print("Recursive Fibonacci:")
	print(*fibonacci_sequence_recursive(n))

# --- Comparison Report ---
# Execution Flow:
# Iterative: Updates two variables in a loop, appends each term.
# Recursive: Calls itself for each term, builds sequence by repeated function calls.
#
# Time Complexity:
# Iterative: O(n)
# Recursive: O(2^n) (naive, exponential)
#
# Space Complexity:
# Iterative: O(n) for result list
# Recursive: O(n) for call stack, O(n) for result list
#
# Performance for Large n:
# Iterative: Fast and efficient for large n
# Recursive: Very slow for large n due to repeated calculations
#
# When to Avoid Recursion:
# For large n, recursion is inefficient and may cause stack overflow. Prefer iteration for performance and reliability.
