import numpy as np

# numpyのastypeメゾットを使って返り値をboolからintに変換する.
x = np.array([-1.0, 1.0, 2.0])
print(x)
y = x > 0
print(y)
y = y.astype(np.int)
print(y)
