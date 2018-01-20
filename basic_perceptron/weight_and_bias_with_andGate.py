import numpy as np
# Implement Wight & Bias into AND gate method

# (w1*x1)+(w2*x2) <= M >>>> y=0
# (w1*x1)+(w2*x2) > M >>>>> y=1

# (w1*x1)+(w2*x2)+b <= 0 >>>> y=0
# (w1*x1)+(w2*x2)+b > 0  >>>> y=1



def AND(x1, x2):
    x = np.array([x1, x2]) # Input(入力値)
    w = np.array([0.5, 0.5]) # Weight(重み)
    b = -0.7
    tmp = np.sum(x*w) + b
    print(tmp)
    if tmp <= 0: # (w1*x1)+(w2*x2)+b <= 0
        print("zero")
        return 0
    else: # (w1*x1)+(w2*x2)+b > 0
        print("one")
        return 1


# Call method
AND(0, 0) # return 1 [(0*0.5)+(0*0.5)]+(-0.7)
AND(-1, 0) # return 0
AND(1, 1) # return 0 [(1*0.5)+(1*0.5)]+(-0.7)
AND(-1, -1) # return 0 [(-1*0.5)+(-1*0.5)]+(-0.7) = -1.7 < 0
