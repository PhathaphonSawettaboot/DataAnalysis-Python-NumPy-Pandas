import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn.tree import plot_tree

# Read the dataset (example: iris dataset)
data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# Convert categorical species column to numerical using LabelEncoder
label_encoder = LabelEncoder()
data['encoded_species'] = label_encoder.fit_transform(data['species'])

# Set features and target columns
X = data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = data['encoded_species']

# Create a Decision Tree model
model = DecisionTreeClassifier()

# Split the dataset and train the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)

# Result Explained (Feature Importance)
feature_importance = model.feature_importances_
print("Feature Importance:", feature_importance)

# Display Tree
plt.figure(figsize=(10, 6))
plot_tree(model, filled=True, feature_names=X.columns.tolist(), class_names=label_encoder.classes_.tolist())
plt.show()

# Predict Values
predictions = model.predict(X_test)

# Model Evaluation
accuracy = accuracy_score(y_test, predictions)
classification_rep = classification_report(y_test, predictions)
conf_matrix = confusion_matrix(y_test, predictions)

print("Accuracy:", accuracy)
print("Classification Report:\n", classification_rep)
print("Confusion Matrix:\n", conf_matrix)

# Seaborn Heat Map
sns.heatmap(conf_matrix, annot=True, cmap="Blues")
plt.xlabel("Predicted Labels")
plt.ylabel("True Labels")
plt.title("Confusion Matrix Heatmap")
plt.show()

# k-Fold Cross Validation
scores = cross_val_score(model, X, y, cv=5)
mean_accuracy = scores.mean()
print("Mean Accuracy from Cross Validation:", mean_accuracy)
