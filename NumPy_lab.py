import pandas as pd

# Creating a DataFrame with duplicates
data = {'Name': ['Alice', 'Bob', 'Alice', 'David'],
        'Age': [25, 30, 25, 22]}
df = pd.DataFrame(data)

# Check for duplicates
print(df.duplicated())

# Drop duplicates
df.drop_duplicates(inplace=True)
