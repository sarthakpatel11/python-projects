from numpy.lib.function_base import insert
from numpy.random.mtrand import rand, randn, seed
import pandas as pd
import numpy as np


# labales = ['a', 'b', 'c']
# my_data = [1, 2, 3]
# arr = np.array(my_data)
# d = {"a": 1, "b": 2, "c": 3}
# print(pd.Series(data=my_data))
# print(pd.Series(data=my_data, index=labales))
# print(pd.Series(arr))
# print(pd.Series(d))


#  ////////////////////////////////
# from numpy.random import randn
# np.random.seed(101)
df = pd.DataFrame(randn(4, 4), ['a', 'b', 'c', 'd'], ['w', 'x', 'y', 'z'])
# print(df)
# print(df['w'])
# print(df[['w', 'z']])
# df['new'] = df['w'] + df['y']
# print(df)
# print(df.shape)
# print(df.drop('new', axis=1))
# print(df.loc['a'])
# print(df.iloc[0])  # is equal to upper line
# print(df.loc['b', 'y'])    # give particular value
# print(df.loc[['a', 'b'], ['z', 'y']])


#  ////////////////////////////////
# outside = ['g1', 'g1', 'g1', 'g2', 'g2', 'g2']
# inside = [1, 2, 3, 1, 2, 3]
# hier_index = list(zip(outside, inside))
# hier_index = pd.MultiIndex.from_tuples(hier_index)
# print(outside)
# print(inside)
# print(list(zip(outside, inside)))
# print(hier_index)

# df = pd.DataFrame(randn(6, 2), hier_index, ['a', 'b'])
# print(df)
# print(df.loc['g1'])
# print(df.loc['g1'].loc[1])

# df.index.names = ["group", "num"]
# print(df)
# print(df.loc['g2'].iloc[1, 1])
# print(df.loc['g2'].loc[2]['b'])
# print(df.xs(1, level='num'))
# print(df.xs('g1'))
