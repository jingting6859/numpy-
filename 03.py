import numpy as np
import pandas as pd

a = pd.DataFrame(np.ones((3,4)),columns=list('abcg'))
b = pd.DataFrame(np.zeros((3,4)),columns=list('defg'))

a['g']=[3,3,3]
b['g']=[3,3,3]
print(a)
print(b)

d = pd.merge(a,b,on='g',how='inner')
print(d)
