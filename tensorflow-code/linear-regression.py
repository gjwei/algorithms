# coding: utf-8
# Author: gjwei
import tensorflow as tf
import numpy as np

learning_rate = 0.001
epochs = 1000
n_dim = 5

x = np.random.rand(100, 5)
y = np.random.randint(low=1, high=10, size=(100, 1))

X = tf.placeholder(dtype=tf.float32, shape=[None, 5])
Y = tf.placeholder(dtype=tf.float32, shape=[None, 1])

W = tf.get_variable('W', shape=[n_dim, 1], initializer=tf.random_normal_initializer())
b = tf.get_variable('b', shape=[None, 1], initializer=tf.zeros_initializer())

init = tf.initialize_all_variables()

logit = tf.add(tf.matmul(X, W), b)

loss = tf.reduce_mean(tf.square(logit - y))
train_op = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(loss)

sess = tf.Session()
sess.run(init)

loss = []

for epoch in range(1, epochs + 1):
    batch_cost, _ = sess.run([loss, train_op],
                             feed_dict={X: x, Y: y})

