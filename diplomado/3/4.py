import matplotlib.pyplot as mpl
import pandas as pd


df = pd.DataFrame([
   [1., .5, 32, 5], 
   [1., .7, 45, 7],
   [7., .3, 51, 3],
   [2., .4, 23, 4]],
   index=['a', 'b', 'c', 'd'],
   columns=['c1', 'c2', 'c3','c4']
)

series = pd.Series(['a','b','c'])

print(df.describe())

# print(df.c2)
# df.c1.fillna(df.c1.mean(), inplace=True)

"""
mpl.plot(df.c1)
mpl.plot(df.c2)
mpl.plot(df.c3)
mpl.show()
"""