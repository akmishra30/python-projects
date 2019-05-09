import tensorflow as tf

slope = tf.Variable([.4], tf.float32)
bias = tf.Variable([-0.4], tf.float32)

x = tf.placeholder(tf.float32)

linear_model = slope * x + bias

sess = tf.Session()
init = tf.global_variables_initializer()

sess.run(init)

print(sess.run(linear_model, {x: [1, 2, 3, 4]}))