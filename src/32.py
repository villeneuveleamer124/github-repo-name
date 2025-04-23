import matplotlib.pyplot as plt
import numpy as np

def plot_sin_wave(x_values, y_values):
    """
    Plots a sin wave using given x and y data.
    Args:
        x_values: A sequence of x values.
        y_values: A sequence of y values for the sin wave.

    Returns:
        None
    """
    plt.plot(x_values, y_values)
    plt.title("Sin Wave")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.show()

# Example usage:
x = np.linspace(0, 10, 50)  # Generate x values
y = np.sin(x)             # Calculate the sin wave

plot_sin_wave(x, y)
