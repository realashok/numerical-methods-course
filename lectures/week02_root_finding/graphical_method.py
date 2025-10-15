import numpy as np
import matplotlib.pyplot as plt
import os

def f(x):
    return np.sin(10*x) + np.cos(3*x)

x = np.linspace(0, 5, 50001)
y = f(x)

# Plot the function
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='f(x) = sin(10x) + cos(3x)')
plt.axhline(0, color='black', linewidth=0.8)  # x-axis
plt.title('Graphical Method: f(x) = sin(10x) + cos(3x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(alpha=0.4)
plt.legend()

plt.minorticks_on()  # turn on minor ticks
plt.grid(which='major', linestyle='-', linewidth=0.7, alpha=0.8)
plt.grid(which='minor', linestyle=':', linewidth=0.5, alpha=0.5)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
plot_path = os.path.join(SCRIPT_DIR, 'graph.png')
plt.savefig(plot_path, dpi=300)
