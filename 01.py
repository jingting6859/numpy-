import numpy as np

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
print(arr1.__add__(10))
# [[3,12, 21],[30,39,48],[57,66,75]]
# #

# print(arr1.item())
# x= np.array([1,2,3])
# print(arr1.tofile('01.txt'))
# print(arr1.dtype)
# for i in arr1.flat:
#     print(type(i))
#     print(type(i.item()))
# print(arr1[1][2])
# y = arr1[:,1]
# print(y)
# y[0] = 9
# print(y)
# print(arr1)

# constructing arrays 构造数组
#   Array attributes¶

# ndarray.flags	Information about the memory layout of the array.
# ndarray.shape	Tuple of array dimensions.
# ndarray.strides	Tuple of bytes to step in each dimension when traversing an array.(12, 4)
# ndarray.ndim	Number of array dimensions.  数组的维度数
# ndarray.data	Python buffer object pointing to the start of the array’s data.  <memory at 0x048E7558>
# ndarray.size	Number of elements in the array.
# ndarray.itemsize	Length of one array element in bytes. 数组每个元素的字节数
# ndarray.nbytes	Total bytes consumed by the elements of the array.  所有元素的字节总数
# ndarray.base	Base object if memory is from some other object.

# ndarray.T	The transposed array.
# ndarray.real	The real part of the array. 原始数组
# ndarray.imag	The imaginary part of the array. [[0 0 0][0 0 0]]  数组的虚部
# ndarray.flat	A 1-D iterator over the array.  <numpy.flatiter object at 0x04CB0E70> 数组上的一维迭代
# ndarray.ctypes	An object to simplify the interaction of the array with the ctypes module. <numpy.core._internal._ctypes object at 0x02BAEBF0>

# __array_interface__	Python-side of the array interface
# __array_struct__	C-side of the array interface


# numpy yu list 之间的转换
# ndarray.item(*args)	Copy an element of an array to a standard Python scalar and return it.
# ndarray.tolist()	Return the array as an a.ndim-levels deep nested list of Python scalars.
# ndarray.itemset(*args)	Insert scalar into an array (scalar is cast to array’s dtype, if possible)
# ndarray.tostring([order])	Construct Python bytes containing the raw data bytes in the array.
# ndarray.tobytes([order])	Construct Python bytes containing the raw data bytes in the array.
# ndarray.tofile(fid[, sep, format])	Write array to a file as text or binary (default).
# ndarray.dump(file)	Dump a pickle of the array to the specified file.
# ndarray.dumps()	Returns the pickle of the array as a string.
# ndarray.astype(dtype[, order, casting, …])	Copy of the array, cast to a specified type.
# ndarray.byteswap([inplace])	Swap the bytes of the array elements
# ndarray.copy([order])	Return a copy of the array.
# ndarray.view([dtype, type])	New view of array with the same data.
# ndarray.getfield(dtype[, offset])	Returns a field of the given array as a certain type.
# ndarray.setflags([write, align, uic])	Set array flags WRITEABLE, ALIGNED, (WRITEBACKIFCOPY and UPDATEIFCOPY), respectively.
# ndarray.fill(value)	Fill the array with a scalar value.


#
# ndarray.take(indices[, axis, out, mode])	Return an array formed from the elements of a at the given indices.
# ndarray.put(indices, values[, mode])	Set a.flat[n] = values[n] for all n in indices.
# ndarray.repeat(repeats[, axis])	Repeat elements of an array.
# ndarray.choose(choices[, out, mode])	Use an index array to construct a new array from a set of choices.
# ndarray.sort([axis, kind, order])	Sort an array in-place.
# ndarray.argsort([axis, kind, order])	Returns the indices that would sort this array.
# ndarray.partition(kth[, axis, kind, order])	Rearranges the elements in the array in such a way that the value of the element in kth position is in the position it would be in a sorted array.
# ndarray.argpartition(kth[, axis, kind, order])	Returns the indices that would partition this array.
# ndarray.searchsorted(v[, side, sorter])	Find indices where elements of v should be inserted in a to maintain order.
# ndarray.nonzero()	Return the indices of the elements that are non-zero.
# ndarray.compress(condition[, axis, out])	Return selected slices of this array along given axis.
# ndarray.diagonal([offset, axis1, axis2])	Return specified diagonals.


#比较
# ndarray.__lt__(self, value, /)	Return self<value.
# ndarray.__le__(self, value, /)	Return self<=value.
# ndarray.__gt__(self, value, /)	Return self>value.
# ndarray.__ge__(self, value, /)	Return self>=value.
# ndarray.__eq__(self, value, /)	Return self==value.
# ndarray.__ne__(self, value, /)	Return self!=value.

# ndarray.__add__(self, value, /)	Return self+value.
# ndarray.__sub__(self, value, /)	Return self-value.
# ndarray.__mul__(self, value, /)	Return self*value.
# ndarray.__truediv__(self, value, /)	Return self/value.
# ndarray.__floordiv__(self, value, /)	Return self//value.
# ndarray.__mod__(self, value, /)	Return self%value.
# ndarray.__divmod__(self, value, /)	Return divmod(self, value).
# ndarray.__pow__(self, value[, mod])	Return pow(self, value, mod).
# ndarray.__lshift__(self, value, /)	Return self<<value.
# ndarray.__rshift__(self, value, /)	Return self>>value.
# ndarray.__and__(self, value, /)	Return self&value.
# ndarray.__or__(self, value, /)	Return self|value.
# ndarray.__xor__(self, value, /)	Return self^value.

# ndarray.__copy__()	Used if copy.copy is called on an array.
# ndarray.__deepcopy__()	Used if copy.deepcopy is called on an array.
# ndarray.__reduce__()	For pickling.
# ndarray.__setstate__(state, /)	For unpickling.
# Basic customization:
#
# ndarray.__new__(\*args, \*\*kwargs)	Create and return a new object.
# ndarray.__array__()	Returns either a new reference to self if dtype is not given or a new array of provided data type if dtype is different from the current dtype of the array.
# ndarray.__array_wrap__()
# Container customization: (see Indexing)
#
# ndarray.__len__(self, /)	Return len(self).
# ndarray.__getitem__(self, key, /)	Return self[key].
# ndarray.__setitem__(self, key, value, /)	Set self[key] to value.
# ndarray.__contains__(self, key, /)	Return key in self.
#dtype###########################################################################################################
# number, inexact, floating	float
# complexfloating	cfloat
# integer, signedinteger	int_
# unsignedinteger	uint
# character	string
# generic, flexible	void
#1.
np.array((2,3))