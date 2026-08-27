import tensorflow as tf
import numpy as np
import keras
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
xs = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=float)
ys = np.array([1.0, 6.0, 13.0, 24.0, 37.0, 54.0], dtype=float)
model.compile(optimizer='sgd', loss='mean_squared_error')
model.fit(xs,ys,epochs=100)
print(model.predict(np.array([10])))