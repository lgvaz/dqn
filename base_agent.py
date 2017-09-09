import numpy as np
import tensorflow as tf

class BaseAgent:
    def __init__(self, env):
        self.env = env
        self.state = env.reset()
        self.sess = None

    def _maybe_create_tf_sess(self):
        if self.sess is None:
            self.sess = tf.Session()
            self.sess.run(tf.global_variables_initializer())

    def select_action(self):
        raise NotImplementedError