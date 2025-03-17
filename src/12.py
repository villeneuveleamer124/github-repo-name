import random
def generate_random_python_code():
    """
    Generates a random Python code snippet of length 10 to 20 characters.
    :return: A random Python code snippet of length 10 to 20 characters.
    """
    code = ''
    for i in range(random.randint(10, 20)):
        code += chr(random.randint(97, 122))
    return code