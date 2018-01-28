import numpy as np
import matplotlib.pylab as plt

#ソフトマックス関数の出力の総和は1となる。
# Sigmoid function
def Sigmoid(x):
    result = 1 / (1 + np.exp(-x)) # exp = 2.7182
    print("Sigmoid output >> " + str(result))
    return result

