import numpy as np
import matplotlib.pylab as plt


# Sigmoid function(シグモイド関数)
def sigmoid(x):
    ans = 1 / (1 + np.exp(-x)) # exp = 2.7182 ......
    print(ans)
    return ans


# STEP関数(階段関数)
def step_function(x):
    return np.array(x > 0, dtype=np.int)


# Create graph info
x = np.arange(-5.0, 5.0, 0.1) # レンジ設定
plt.ylim(-0.1, 1.1) # y軸の範囲を指定

# Sigmoid func
y_sigmoid = sigmoid(x)
plt.plot(x, y_sigmoid)

# Step func
y_step = step_function(x)
plt.plot(x, y_step, linestyle="--")

# Show
plt.show()
