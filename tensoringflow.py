import tensorflow as tf
import keras
import numpy as np
model = tf.keras.models([
    keras.layers.Conv2D(input_shape=(28,28)),
    keras.layers.Dense(64, (3,3), activation = "relu"
                          ,input_shape=(28,28,1)),
    keras.layers.MaxPooling2D(2,2),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])
