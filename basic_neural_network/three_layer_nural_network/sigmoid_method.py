import numpy as np
import matplotlib.pylab as plt


# Sigmoid function
def Sigmoid(x):
    result = 1 / (1 + np.exp(-x)) # exp = 2.7182
    print("Sigmoid output >> " + str(result))
    return result

