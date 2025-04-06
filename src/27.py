def calculate_average(numbers):
    if not numbers:
        return 0
    else:
        total = sum(numbers)
        average = total / len(numbers)
        return average

numbers = [1, 2, 3, 4, 5]
average = calculate_average(numbers)
print("The average is:", average)
