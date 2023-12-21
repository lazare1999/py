import pandas as pd

# Creating the pandas dataframes from Dictionary
student_data = {'name': ['Jack', 'Riti', 'Aadi'],  # Define dictionary
                'age': [34, 30, 16],
                'city': ['Sydney', 'Delhi', 'New york']}
s_df = pd.DataFrame(student_data)

# selecting the rows based on column values
print(s_df.loc[s_df['name'] == 'Riti'])
print(s_df.loc[s_df['city'].isin(['Sydney', 'Delhi'])])
print(s_df.loc[(s_df['age'] >= 20) & (s_df['name'] == 'Jack')])

# adding new rows to pandas dataframe
new_student_data = {'name': ['lazo', 'mari'],  # Define dictionary
                    'age': [23, 25],
                    'city': ['Tbilisi', 'Tbilisi']}

s_df_2 = pd.DataFrame(new_student_data)
result = pd.concat([s_df, s_df_2])
print(result)
