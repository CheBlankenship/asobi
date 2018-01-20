import numpy as np

# ニューラルネットワークの行列の積
# x配列の要素数がw配列の要素数と２として一致する。
x = np.array([1,2])
x_shape = x.shape
print(x_shape)

w = np.array([[1,3,5], [2,4,6]])
w_shape = w.shape
print(w_shape)

dot_x_and_w = np.dot(x,w)
# (1*1)+(2*2)=5
# (1*3)+(2*4)=11
# (1*5)+(2*6)=17

print(dot_x_and_w)
