import numpy as np
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 25, 12, 40, 30]

plt.bar(categories, values, color= 'orange')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Line Plot')
plt.grid(True)
plt.show()