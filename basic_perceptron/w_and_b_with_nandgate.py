import numpy as np
# Implement Wight & Bias into OR gate method

# (w1*x1)+(w2*x2) <= M >>>> y=0
# (w1*x1)+(w2*x2) > M >>>>> y=1

# (w1*x1)+(w2*x2)+b <= 0 >>>> y=1
# (w1*x1)+(w2*x2)+b > 0  >>>> y=0



def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        print("zero")
        return 0
    else:
        print("one")
        return 1


NAND(0, 0) # return 1 [(0*0.5)+(0*0.5)]+(-0.7) = -0.7 < 0  (y=1)
NAND(1, 1) # return 0 [(1*0.5)+(1*0.5)]+(-0.7) = 0.3 >= 0  (y=0)
NAND(0, 1) # return
NAND(1, 0)
