import numpy as np
import matplotlib.pylab as plt

# STEP関数(階段関数)
def step_function(x):
    return np.array(x > 0, dtype=np.int)

x = np.arange(-5.0, 5.0, 0.1) #-0.5から5.0まで0.1刻みで
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) # y軸の範囲を指定
plt.show()
