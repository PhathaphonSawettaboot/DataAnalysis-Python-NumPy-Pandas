import pandas as pd

data = {'A' : [1,2,2,3,4,4],
        'B' : ['apple', 'banana', 'banana', 'orange', 'apple', 'apple']}

df = pd.DataFrame(data)

df_no_duplicates = df.drop_duplicates()
print("DataFrame with Duplicates Removed: ", df_no_duplicates)