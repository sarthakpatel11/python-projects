import numpy as np
from numpy.core.fromnumeric import mean
import pandas as pd


# #  missing values
d = {'a': [1, 2, np.nan], 'b': [5, np.nan, np.nan], 'c': [1, 2, 3]}
df = pd.DataFrame(d)
# print(df)
# print(df.dropna())
# print(df.dropna(axis=1))
# print(df.dropna(thresh=2))

# # filling missing values

# print(df.fillna(value=3))
# print(df['a'].fillna(value=df['a'].mean()))
data = {'company': ['goog', 'goog', 'msft', 'msft', 'fb', 'fb'],
        'person': ['sam', 'charlie', 'amy', 'vanessa', 'carl', 'sarah'],
        'sales': [200, 120, 340, 124, 243, 350]}
df = pd.DataFrame(data)
# print(df)
df_groupby = df.groupby('company')
# print(df_groupby.mean())
# print(df_groupby.sum())
# print(df_groupby.std())
# # is equal to = df.groupby('cpmpany').sum().loc['fb']
print(df_groupby.sum().loc['fb'])
# print(df_groupby.count())
# print(df_groupby.max())
# print(df_groupby.min())
# print(df_groupby.describe())
# print(df_groupby.describe().transpose()['fb'])


# #  ///////////////////////// opretion
# print(df['company'].unique())
# print(df['company'].nunique())
# print(df['company'].())
# print(df[df['sales'] > 200])
# print(df[(df['sales'] > 200) & (df['company'] == 'fb')])


def times2(x):
    return x*2


print(df['sales'].apply(times2))
