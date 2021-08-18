import sys

sys.path.append('.')

import projectaile as pai

import tensorflow as tf


@pai.MODEL
def model():
    return tf.keras.applications.vgg16.VGG16(weights=None, include_top=False)

model