import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a plot
plt.plot(x, y1, label='Sine Function')
plt.plot(x, y2, label='Cosine Function')

# Add a legend
plt.legend()

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine and Cosine Functions')

# Show the plot
plt.show()