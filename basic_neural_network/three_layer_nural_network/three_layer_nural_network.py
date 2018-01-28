import numpy as np
import matplotlib.pylab as plt
from sigmoid_method import Sigmoid as sigmoid

# y =  {(wx + WX <= θ) = 0 | (wx + WX <= θ) = 1}
# Initializer(ネットワークのディクショナリを定義).
def init_network():
    network = {} #
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.5]]) # Weight one
    network['b1'] = np.array([0.1, 0.2, 0.3]) # Bias one
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]]) # Weight two
    network['b2'] = np.array([[0.1, 0.2]]) # Bias Two
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]]) # Weight three
    network['b3'] = np.array([0.1, 0.2]) # Bias three
    return network


# Activation function for the output(出力層の活性化関数).
def identify_function(x):
    print("Identify the nural network >> ", str(x))
    return x


# Send the output to the next layer(出力方向への伝達処理を行う関数).
def forward(network, x):
    # Define Weights()
    W1 = network['W1'] # [[ 0.1,  0.3,  0.5], [ 0.2,  0.4,  0.5]]
    W2 = network['W2'] # [[ 0.1,  0.4], [ 0.2,  0.5], [ 0.3,  0.6]],
    W3 = network['W3'] # [[ 0.1,  0.3], [ 0.2,  0.4]]
    # Define Biases
    b1 = network['b1'] # [0.1, 0.2, 0.3]
    b2 = network['b2'] # [0.1, 0.2]]
    b3 = network['b3'] # [0.1, 0.2]
    
    # Use DOT multiplication (ドット積)
    a1 = np.dot(x, W1) + b1 # First layer
    z1 = sigmoid(a1) # Return the output using sigmoid method
    #
    a2 = np.dot(z1, W2) + b2 # Second layer
    z2 = sigmoid(a2) # Return the output using sigmoid method
    #
    a3 = np.dot(z2, W3) + b3 # Third layer(aggrigate the input using dot multiplication)
    #
    y = identify_function(a3) # Output
    return y



network = init_network() # Define the weights and biases.
x = np.array([0.1, 0.5]) # Input signal x1 and x2.
y = forward(network, x) # Trigger forward method.
print("Final result >> " + str(y))


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
#
