import sys

sys.path.append('.')

import projectaile as pai

import tensorflow as tf

model = pai.MODEL(tf.keras.applications.vgg16.VGG16(include_top=True, weights=None))

print(type(model))