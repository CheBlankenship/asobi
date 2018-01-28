import numpy as np


## ソフトマックス関数の概要 ##
# ** = 累乗
# exp(x) = E**x (E=2.7182...のネイピア数)
# e**x = M (x = log_x M) 指数関数

# 公式 #
# i = 1
# n = undefined
# k = undefined
# y_k = 指数関数 / 指数関数の和
# y_k = exp(a_k) / i_Σ_n exp(a_i)


# [Step 0]
a = np.array([0.3, 2.9, 4.0]) # 入力信号

# [Step 1]
exp_a = np.exp(a) # 指数関数
# 解説 #
# k = 0
# a[k] = a[0] = 0.3
# exp(x) = E**x
# E = (E=2.7182...のネイピア数)
# result = exp(a[0]) = exp(0.3) = E**0.3 = 2.7182**0.3
# result = 1.34985881
print("exp_a >> " + str(exp_a)) # [1.34985881, 18.174114537, 54.59815003]

# [Step 2]
sum_exp_a = np.sum(exp_a) # numpyのsum()で配列として出力された指数関数の和を求める。
print("sum_exp >> " + str(sum_exp_a))

# [Step 3]
# y_k = 指数関数 / 指数関数の和
y = exp_a / sum_exp_a
print("y >> " + str(y))


## Output ##
#exp_a >> [  1.34985881  18.17414537  54.59815003]
#sum_exp >> 74.1221542102
#y >> [ 0.01821127  0.24519181  0.73659691]

