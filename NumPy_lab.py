import pandas as pd

data = {'A' : [1,2,3],
        'B' : [4,5,6],
        'C' : [7,8,9]}

df = pd.DataFrame(data)

column_sums = df.sum(axis=0)
print("Column : ", column_sums)

row_sums = df.sum(axis=1)
print("Row Sums: ", row_sums)