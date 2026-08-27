import tensorflow_probability as tfp
import tensorflow as tf
tfd= tfp.distributions
initial_distribution=tfd.categorical(probs=[0.8,0.2])
transition_distribution= tfd.categorical(probs=[[0.7,0.3],
                                              [0.2,0.8]])
observation_distribution=tfd.normal(loc=[0.,15.], scale=[5., 10.])