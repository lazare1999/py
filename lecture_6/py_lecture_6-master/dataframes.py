import pandas as pd

list_of_lists = [['January', 31],
                 ['February', 28],
                 ['March', 31]]

# load data into a DataFrame object:
df = pd.DataFrame(list_of_lists)

print(df)

# create dict of lists
dict_of_lists = {
    'Students': ['Alan', 'Vivian', 'Alister', 'Jade'],
    'Age': [24, 26, 32, 29]
}

# creating the DataFrame
df1 = pd.DataFrame(dict_of_lists)
print(df1)

print(df1.loc[df1['Students'] == 'Alan'])

# To select rows whose column value is in an iterable, some_values, use isin:
print(df1.loc[df1['Students'].isin(['Alan', 'Alister'])])

# Combine multiple conditions with &:
print(df1.loc[(df1['Age'] >= 20) & (df1['Students'] == 'Jade')])

# create dict of lists
dict_of_lists_2 = {
    'Students': ['lazo', 'mari'],
    'Age': [23, 25]
}

df2 = pd.DataFrame(dict_of_lists_2)
result = pd.concat([df1, df2])
print(result)

print(result.iloc[2:6, 0:1])

# Initializing the nested list with Data set
player_list = [['M.S.Dhoni', 36, 75, 5428000],
               ['A.B.D Villers', 38, 74, 3428000],
               ['V.Kholi', 31, 70, 8428000],
               ['S.Smith', 34, 80, 4428000],
               ['C.Gayle', 40, 100, 4528000],
               ['J.Root', 33, 72, 7028000],
               ['K.Peterson', 42, 85, 2528000]]

# creating a pandas dataframe
df3 = pd.DataFrame(player_list, columns=['Name', 'Age', 'Weight', 'Salary'])

print(df3)
print("---------------------------------------")
# Sorting by column 'Weight'
df4 = df3.sort_values(by=['Weight'])
print(df4)

Class = [0, 0, 0, 0, 1, 1, 1]
df4['class'] = Class
print(df4)