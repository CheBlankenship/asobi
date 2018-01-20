import numpy as np

# dot function(ドット積)
# 行列の積の計算

a = np.array([[1,2],[3,4]])
a_shape = a.shape
print(a_shape)

b = np.array([[5,6],[7,8]])
b_shape = b.shape
print(b_shape)

numpy_dot = np.dot(a,b)
# (1*5)+(2*7)=19
# (1*6)+(2*8)=22
# (3*5)+(4*7)=43
# (3*6)+(4*8)=50
print(numpy_dot)


