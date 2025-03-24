def add_numbers(a, b):
    """
    Adds two numbers.
    :param a: First number
    :type a: int or float
    :param b: Second number
    :type b: int or float
    :return: Sum of a and b
    :rtype: int or float
    """
    return a + b

def calculate_total(numbers):
    """
    Calculates the sum of all numbers in a list.
    :param numbers: A list of numbers
    :type numbers: list
    :return: Total sum of the numbers in the list
    :rtype: int or float
    """
    total = 0
    for number in numbers:
        total += number
    return total

# Example usage
a = 5.0
b = 3.0
print("The sum of", a, "and", b, "is:", add_numbers(a, b))

numbers = [1.5, 2.7, 3.8, 4.9]
total = calculate_total(numbers)
print("The total is:", total)
