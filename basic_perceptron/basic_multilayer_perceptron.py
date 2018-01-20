import numpy as np

# Define AND Gate Method
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

# Define NAND Gate Method
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

# Define OR Gate Method
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


# Setup basic XOR Gate Method
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    print("Result >> "+str(y))
    return y


XOR(1,1) # NAND=> 0, OR=>1, XOR=>0
XOR(0,1) # NAND=> 1, OR=>1, XOR=>1
XOR(1,0) # NAND=> 1, OR=>1, XOR=>1
XOR(0,0) # NAND=> 1, OR=>0, XOR=>0




