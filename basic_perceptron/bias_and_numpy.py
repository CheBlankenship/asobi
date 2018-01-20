import numpy as np

x = np.array([0, 1]) # Input(入力)
w = np.array([0.5, 0.5]) # Weight(重み)
b = -0.7 # Bias バイアス

multi = x * w
print(multi) #[0. 0.5]

sum_numpy = np.sum(x*w)
print(sum_numpy) #0.5

bias_sum_num = np.sum(x*w) + b

print(bias_sum_num) #-0.2(四捨五入)
