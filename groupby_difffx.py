import numpy as np
import pandas as pd
import pdb
from scipy.stats import circmean
import math

df = pd.DataFrame(np.random.rand(4,4), columns=list('abcd'))
df['group'] = [0, 0, 1, 1]

# Primer paso convertir todo a radianes

pdb.set_trace()
df['a'] = math.radians(df.a)
print('hola')

df = pd.DataFrame(np.random.rand(4,4), columns=list('abcd'))
df['group'] = [0, 0, 1, 1]
df

def max_min(x):
    return x.max() - x.min()

max_min.__name__ = 'Max minus Min'

df.groupby('group').agg({'a':['sum', 'max'],
                         'b':'mean',
                         'c':'sum',
                         'd': max_min})

#               a                   b         c             d
#             sum       max      mean       sum Max minus Min
# group
# 0      0.864569  0.446069  0.466054  0.969921      0.341399
# 1      1.478872  0.843026  0.687672  1.754877      0.672401
