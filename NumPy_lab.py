import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22]}
df = pd.DataFrame(data)

# Adding a new row by index
new_row = pd.Series({'Name': 'David', 'Age': 28})
df = pd.concat([df, new_row.to_frame().T], ignore_index=True)

# Deleting a row by index
df.drop(1, inplace=True)  # Delete the row with index 1

# Adding a new row by key (dictionary)
new_row_dict = {'Name': 'Eve', 'Age': 29}
new_row_df = pd.DataFrame(new_row_dict, index=[len(df)])  # Create a DataFrame for the new row
df = pd.concat([df, new_row_df], ignore_index=True)  # Concatenate the original DataFrame and the new row DataFrame

# Deleting a row by key (condition)
df = df[df['Name'] != 'Charlie']  # Delete rows where the 'Name' is 'Charlie'

print(df)



