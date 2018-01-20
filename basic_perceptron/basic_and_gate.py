# basic perceptron method

def AND(x1, x2):
    w1 = 0.5
    w2 = 0.7
    theta = 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        print("zero")
        return 0
    elif tmp > theta:
        print("one")
        return 1

AND(0, 0) # return 0
AND(1, 0) # return 0
AND(0, 1) # return 0
AND(1, 1) # return 1
