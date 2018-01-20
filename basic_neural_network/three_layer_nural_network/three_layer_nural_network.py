import numpy as np
import matplotlib.pylab as plt
from sigmoid_method import Sigmoid as sigmoid


#
def init_network():
    network = {} #
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.5]]) # Weight one
    network['b1'] = np.array([0.1, 0.2, 0.3]) # Bias one
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]]) # Weight two
    network['b2'] = np.array([[0.1, 0.2]]) # Bias Two
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]]) # Weight three
    network['b3'] = np.array([0.1, 0.2]) # Bias three
    return network


## Network object ##
#{
#    'W1': [[ 0.1,  0.3,  0.5], [ 0.2,  0.4,  0.5]],
#    'b1': [ 0.1,  0.2,  0.3],
#    'W2': [
#       [ 0.1,  0.4],
#       [ 0.2,  0.5],
#       [ 0.3,  0.6]
#     ],
#     'b2': [[ 0.1,  0.2]],
#     'W3': [
#       [ 0.1,  0.3],
#       [ 0.2,  0.4]
#      ],
#      'b3': [ 0.1,  0.2]
#}


#
def identify_function(x):
    print("Identify the nural network >> ", str(x))
    return x


#
def forward(network, x):
    # Define Weights
    W1 = network['W1']
    W2 = network['W2']
    W3 = network['W3']
    # Define Bias
    b1 = network['b1']
    b2 = network['b2']
    b3 = network['b3']
    #
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    #
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    #
    a3 = np.dot(z2, W3) + b3
    #
    y = identify_function(a3)
    return y



network = init_network()
x = np.array([0.1, 0.5])
y = forward(network, x)
print("Final result >> " + str(y))
