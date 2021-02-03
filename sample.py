import pandas as pd

df1 = pd.DataFrame([['a', 1], ['b', 2]],
                   columns=['letter', 'number'])
# df1
#   letter  number
# 0      a       1
# 1      b       2
df2 = pd.DataFrame([['c', 3], ['d', 4],['a', 1], ['b', 2]],
                   columns=['yo', 'hi'])
# df2
#   letter  number
# 0      c       3
# 1      d       4
pd.concat([df1, df2],ignore_index=True).drop_duplicates()
#   letter  number
# 0      a       1
# 1      b       2
# 0      c       3
# 1      d       4

df1

df2

