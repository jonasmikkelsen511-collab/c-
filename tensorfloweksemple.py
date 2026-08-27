import tensorflow as tf
import numpy as np
import keras
model = tf.keras.Sequential([keras.layers.Dense(units=2, input_shape=[2])])
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
zs = np.array([-1.0, 0.0, 1.0, 4.0, 9.0, 16.0], dtype=float)
model.compile(optimizer='sgd', loss='mean_squared_error')
model.fit(xs,ys,zs,epochs=20)
print(model.predict(np.array([11])))