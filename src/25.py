import random

def generate_random_string(length):
    """
    Generate a random string of a specified length.
    """
    import random
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(random.choice(letters) for _ in range(length))

print(generate_random_string(10))
