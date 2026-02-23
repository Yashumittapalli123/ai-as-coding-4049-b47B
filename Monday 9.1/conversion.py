#generate a pydoc documentation in conversion.py with functions:o decimal_to_binary(n)o binary_to_decimal(b) o decimal_to_hexadecimal(n).
def decimal_to_binary(n):
    """
    Converts a decimal number to its binary representation.

    Parameters:
    n (int): The decimal number to be converted.

    Returns:
    str: The binary representation of the input decimal number.
    """
    return bin(n)[2:]  # Remove the '0b' prefix
def binary_to_decimal(b):
    """
    Converts a binary number (as a string) to its decimal representation.
    Parameters: 
    b (str): The binary number to be converted, represented as a string.
    Returns:
    int: The decimal representation of the input binary number.
    """
    return int(b, 2)  # Convert binary string to decimal integer
def decimal_to_hexadecimal(n):
    """
    Converts a decimal number to its hexadecimal representation.

    Parameters:
    n (int): The decimal number to be converted.

    Returns:
    str: The hexadecimal representation of the input decimal number.
    """
    return hex(n)[2:]  # Remove the '0x' prefix
