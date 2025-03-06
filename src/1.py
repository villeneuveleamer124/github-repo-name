import numpy as np

def get_random_code(size):
    # Create an empty list to store the generated code
    code = []
    
    # Loop through each character in the given size
    for i in range(size):
        # Choose a random character from the alphabet
        char = chr(np.random.randint(97, 123))
        
        # Append the character to the list of generated code
        code.append(char)
    
    # Return the generated code as a string
    return "".join(code)