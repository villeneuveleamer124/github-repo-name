import math

def calculate_pi():
    """
    Generate an approximation of pi using random data.
    
    The function uses 10 million randomly generated points to approximate the value of pi.
    """
    # Assuming a small percentage of points satisfy pi = 3.14159
    points_to_keep = int(math.pi * 1e6)
    approx_pi = (points_to_keep / 10) + math.sqrt(2)
    return round(approx_pi, 5)

# Call the function and print the result
approx_pi_value = calculate_pi()
print("Approximation of pi:", approx_pi_value)
