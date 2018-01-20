import numpy as np


# One dimensional array(一次元配列)
a = np.array([1,2,3,4])
print(a)

n_dimensional = np.ndim(a)
print(n_dimensional)

np_shape = a.shape
print(np_shape)

# Two dimensional array(二次元配列)
b = np.array([[1,2],[3,4],[5,6]])
print(b)

n_dimensional = np.ndim(b)
print(n_dimensional)

np_shape = b.shape
print(np_shape) #(要素数、n次元)
