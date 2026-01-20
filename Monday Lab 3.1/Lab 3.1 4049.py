def is_palindrome(num):
    if num < 0:
        return False

    original = num
    reverse_num = 0

    while num != 0:
        digit = num % 10
        reverse_num = reverse_num * 10 + digit
        num //= 10

    return original == reverse_num


def factorial(n):
    if n < 0:
        return "Invalid input"

    result = 1
    for value in range(1, n + 1):
        result *= value

    return result

factorial_result = factorial(5)
print(factorial_result)  # Output: 120


def armstrong_check(number):
    if number < 0:
        print("Not an Armstrong Number")
        return

    digits = []
    temp = number

    while temp > 0:
        digits.append(temp % 10)
        temp //= 10

    power = len(digits)
    total = 0

    for d in digits:
        total += d ** power

    if total == number:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")
armstrong_check(153)  # Output: Armstrong Number


def classify_number(n):
    if n < 2:
        print("Neither")
        return

    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            print("Composite")
            return

    print("Prime")
classify_number(29)  # Output: Prime



def perfect_number_check(n):
    if n <= 1:
        print("Not a Perfect Number")
        return

    divisor_sum = 0

    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisor_sum += i

    if divisor_sum == n:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")

perfect_number_check(28)  # Output: Perfect Number



def even_or_odd():
    try:
        value = int(input())
        if value & 1:
            print("Odd")
        else:
            print("Even")
    except:
        return
even_or_odd(3)  # Output: Odd
