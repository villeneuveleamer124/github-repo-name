def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return round(average, 2)

numbers = [10, 20, 30, 40]
print("The average is:", calculate_average(numbers))
