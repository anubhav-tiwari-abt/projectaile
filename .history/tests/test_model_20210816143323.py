import sys

sys.path.append('.')

import projectaile as pai

import tensorflow as tf

model = tf.keras.applications.vgg16.VGG16(weights=None, include_top=False)

model = pai.MODEL(model)