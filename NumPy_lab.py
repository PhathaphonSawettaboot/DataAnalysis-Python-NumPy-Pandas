import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Cathy', 'David'],
        'Age': [25, None, 30, 28]}

df = pd.DataFrame(data)

df['Age'].fillna(0, inplace=True)  # Replace with 0



print(df)
