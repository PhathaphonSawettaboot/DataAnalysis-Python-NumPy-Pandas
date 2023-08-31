import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.array([[1],[2],[3],[4],[5]])
y = np.array([2,3.4,5,6.5,8])

model = LinearRegression()
model.fit(X,y)

predictions = model.predict(X)

plt.scatter(X,y, label='Data')
plt.plot(X, predictions, color='red', label='Linear Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()