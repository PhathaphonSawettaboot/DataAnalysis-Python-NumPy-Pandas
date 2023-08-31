import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Sample data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 4, 9, 16, 25])

# Transform features to higher degrees
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Create and fit the model
model = LinearRegression()
model.fit(X_poly, y)

# Make predictions
X_range = np.linspace(0, 6, 100).reshape(-1, 1)
X_range_poly = poly.transform(X_range)
predictions = model.predict(X_range_poly)

# Plot the data and polynomial regression curve
plt.scatter(X, y, label='Data')
plt.plot(X_range, predictions, color='red', label='Polynomial Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
