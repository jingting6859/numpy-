import pandas as pd
import numpy as np
s = pd.Series([1,2,'dads',np.nan])
pd_data = pd.date_range('2019-1-1',periods=6)
# print(pd_data)
df1 = pd.DataFrame(np.arange(24).reshape((6,4)),columns=['a','b','c','d'],index=pd_data)
# print(df1)
# print(s)
# print(df1.T)
# print(df1.sort_index(axis=0,ascending=False))
# print(df1.sort_values(by='b',ascending=False))
# print(df1['2019-01-02':'2019-01-05'])
#标签
# print(df1.loc['2019-01-02':'2019-01-05','a':'c'])
# # 位置
# print(df1.iloc[1:3,0:2])
#混合
# print(df1.ix[1:5,['a','c']])
# print()
# df1.loc[1,1]=22
df1.a[df1.a>8]=np.nan
# df1[df1.isnull()]=0
# 丢失数据处理
# df2=df1.dropna(axis=1,how='any')
# df2 = df1.fillna(value='xx')/
print(np.any(df1.isnull()==True))
# 导入导出
# concat 合并
a = pd.DataFrame(np.ones((3,4)),columns=list('abcg'),index=[0,1,2])
b = pd.DataFrame(np.zeros((3,4)),columns=list('defg'),index=[1,2,3])
# print(a)

a['g']=[3,3,3]
b['g']=[3,3,3]
print(a)
print(b)

# c = pd.concat([a,b],axis=1,join='outer',join_axes=[a.index])
# s = pd.Series([1,2,3,1],index=list('abcg'))
# # print(c)
# join,merge,append
d = pd.merge(a,b,on='g')
# print(d)
# res = a.append(s,ignore_index=True)
print(d)
