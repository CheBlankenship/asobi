import numpy as np
# Implement Wight & Bias into NAND gate method

# (w1*x1)+(w2*x2) <= M >>>> y=0
# (w1*x1)+(w2*x2) > M >>>>> y=1

# (w1*x1)+(w2*x2)+b <= 0 >>>> y=1
# (w1*x1)+(w2*x2)+b > 0  >>>> y=0


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5]) # ANDとは重みが違う
    b = -0.2                 # ANDとはバイアスが違う
    tmp = np.sum(w*x) + b
    if tmp <=0:
        print("zero")
        return 0
    else:
        print("one")
        return 1


OR(0,0) # return 0
OR(1,1) # return 1
OR(1,0) # return 1
OR(0,1) # return 1
