import numpy as np
a = np.array([1,2,3,4]).reshape((2,2))
# b = np.array(([2,3,4,5])).reshape((2,2))
# print(a)
# print(b)
# print(a*2)
# print('ab:',np.dot(a,b))
# a = np.exp([1,2, 3,4])
a = np.log([2.7,100])
arr1 = np.array(
      [[[ 0,  1,  2],
        [ 3,  4,  5],
        [ 6,  7,  8]],
       [[ 9, 10, 11],
        [12, 13, 14],
        [15, 16, 17]],
       [[18, 19, 20],
        [21, 22, 23],
        [24, 25, 26]]])
a = np.random.randint(1,100,(3,4),dtype=np.int16)
# print(a)
# b=np.sort(a)
# print(b)
# print(a.sum(axis=0))
# print(a.sum(axis=1))
# print(a.max(),a.min())
# b = np.arange(12).reshape((2,6))
# print(b)
# print(np.clip(b,2,9))
# print(np.transpose(b))
# print(np.argmax(b))
# print(np.argmin(b))
# print(np.average(b))
# print(np.median(b))
# print(np.cumsum(b))
# print(np.diff(b))
#索引取值
# b[1][1],b[1,1]b.flat  返回迭代器 b.flatten() 返回所有元素的列表
# 数组合并

# a = np.array([1,1,1])[np.newaxis,:]
# # np.array([])
# b = np.array([2,2,2])[np.newaxis,:]
# # c = np.vstack((a,b))   # 垂直合并
# d = np.hstack((a.T,b.T))   # 水平合并
# print(a.T)
# print(c)
# print(d)

# s数组分割
print(a)
print(np.split(a,4,axis=1))

