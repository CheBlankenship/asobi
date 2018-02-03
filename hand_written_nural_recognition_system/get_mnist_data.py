import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist # import load_mnist method
from PIL import Image # Python Image Library


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img)) # Convert NumPy format to PIL data object
    pil_img.show()


# Load the MNIST dataset by calling load_mnist method
(x_train, t_train), (x_test, t_test) = \
load_mnist(flatten=True, normalize=False, one_hot_label=False)


img = x_train[0]
label = t_train[0]
print(label)

print(img.shape)
img = img.reshape(28, 28)
print(img.shape)

img_show(img)
