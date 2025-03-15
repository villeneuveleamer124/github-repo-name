import random

def get_random_python_code():
    # Generate a random number between 1 and 5
    num = random.randint(1, 5)

    # Return a different piece of python code based on the number generated
    if num == 1:
        return "print('Hello World!')"
    elif num == 2:
        return "for i in range(5):\n\tprint(i)"
    elif num == 3:
        return "numbers = [1, 2, 3, 4, 5]\nfor num in numbers:\n\tprint(num)"
    elif num == 4:
        return "my_list = ['apple', 'banana', 'cherry']\nfor fruit in my_list:\n\tprint(fruit)"
    else:
        return "for i in range(5):\n\tif i % 2 == 0:\n\t\tprint(i)"