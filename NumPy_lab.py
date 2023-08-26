import numpy as np
import matplotlib.pyplot as plt

sizes = [15, 30, 45, 10]

plt.boxplot(sizes)
plt.ylabel('Value')
plt.grid(True)
plt.show()