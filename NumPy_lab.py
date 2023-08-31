import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a sample DataFrame
data = {
    'Age': [25, 30, 35, 40, 45],
    'Income': [50000, 60000, 75000, 90000, 100000],
    'Savings': [10000, 15000, 20000, 25000, 30000],
    'Spending': [3000, 4000, 4500, 5000, 5500]
}
df = pd.DataFrame(data)

# Calculate the correlation matrix
correlation_matrix = df.corr()

# Create the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix Heatmap")
plt.show()
