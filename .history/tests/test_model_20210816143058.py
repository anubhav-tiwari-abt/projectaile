import sys

sys.path.append('.')

import projectaile as pai

import tensorflow as tf


@pai.MODEL
tf.keras.applications.vgg16.VGG16(weights=None, include_top=False)