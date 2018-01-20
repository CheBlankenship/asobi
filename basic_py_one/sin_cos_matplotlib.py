import numpy as np
import matplotlib.pyplot as plt

# Create data
x = np.arange(0, 6, 0.1)
y_one = np.sin(x)
y_two = np.cos(x)


# Write it on a graph
plt.plot(x, y_one, label="sin")
plt.plot(x, y_two, linestyle="--", label="cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin & cos")
plt.legend()
plt.show()

