import numpy as np

# numpyのブロードキャストを用いて、
#次元の異なるが要素数が一致する配列同士を乗算する。

a = np.array([[1,2],[3,4],[5,6]])
a_shape = a.shape
print(a_shape)

b = np.array([7,8])
b_shape = b.shape
print(b_shape)

a_b_dot = np.dot(a,b)
# (1*7)+(2*8)=23
# (3*7)+(4*8)=53
# (5*7)+(6*8)=83
print(a_b_dot)
