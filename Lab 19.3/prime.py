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
