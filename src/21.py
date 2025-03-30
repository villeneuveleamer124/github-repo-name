import random

def generate_random_string(length):
    """
    Generate a random string of a given length.
    
    Args:
        length (int): The length of the generated string.
        
    Returns:
        str: A randomly generated string of the specified length.
    """
    return ''.join(random.choices(['a', 'b', 'c'], k=length))

# Example usage:
random_string = generate_random_string(10)
print(random_string)  # Output a random 10-character string
