import pandas as pd

# Sample data
employees_data = {'Employee_ID': [101, 102, 103, 104],
                  'Name': ['Alice', 'Bob', 'Charlie', 'David'],
                  'Department': ['HR', 'Finance', 'IT', 'Marketing']}
salaries_data = {'Employee_ID': [102, 103, 105, 106],
                 'Salary': [50000, 60000, 55000, 62000]}

employees = pd.DataFrame(employees_data)
salaries = pd.DataFrame(salaries_data)

inner_merge = pd.merge(employees, salaries, on = 'Employee_ID', how = 'inner')
print(inner_merge)

inner_merge = pd.merge(employees, salaries, on = 'Employee_ID', how = 'outer')
print(inner_merge)

inner_merge = pd.merge(employees, salaries, on = 'Employee_ID', how = 'right')
print(inner_merge)