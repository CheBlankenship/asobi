import sys, os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist # load_mnist()を呼び出す

# 最初の呼び出し
(x_train, t_train), (x_test, t_test) = \

# Load the MNIST dataset by calling load_mnist()
load_mnist(flatten=True, normalize=False, one_hot_label=False)

#それぞれのデータの形状を出力
print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)
