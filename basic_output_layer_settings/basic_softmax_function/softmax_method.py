import numpy as np

# ソフトマックス関数
def softmax(a):
    max_input = np.max(a)
    exp_a = np.exp(a - max_input) # Avoid overflow
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y
