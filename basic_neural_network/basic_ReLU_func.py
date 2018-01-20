import numpy as np
import matplotlib.pylab as plt


def ReLU(x):
    return np.maximum(0, x)


#  Create graph data
x = np.arange(-5.0, 5.0, 0.1)


y_relu = ReLU(x)
plt.plot(x, y_relu)

plt.show()
