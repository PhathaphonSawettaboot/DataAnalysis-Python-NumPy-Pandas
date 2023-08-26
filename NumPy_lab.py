import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 25, 12, 40, 30]

plt.scatter(x, y,color= 'pink', marker='o')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')
plt.grid(True)
plt.show()