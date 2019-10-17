import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
from PIL import Image

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# One-hot-encoding uses a vector of binary values to represent numeric or categorical values
# For example, the digit 3 is represented using the vector [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]

n_train = mnist.train.num_examples  # 55,000
n_validation = mnist.validation.num_examples  # 5000
n_test = mnist.test.num_examples  # 10,000

n_input = 784  # input layer (28x28 pixels)
n_hidden1 = 512  # 1st hidden layer
n_hidden2 = 256  # 2nd hidden layer
n_hidden3 = 128  # 3rd hidden layer
n_output = 10  # output layer (0-9 digits)

# hyperparameters
learning_rate = 1e-5    # how much the parameters will adjust at each step of the learning process
n_iterations = 10000     # how many times we go through the training step
batch_size = 128        # how many training examples we are using at each step
dropout = 0.5           # represents a threshold at which we eliminate some units at random (This helps prevent overfitting.)


###############################
#Building the TensorFlow Graph#
###############################

# For X we use a shape of [None, 784], where None represents any amount,
# as we will be feeding in an undefined number of 784-pixel images
X = tf.placeholder("float", [None, n_input])

# The shape of Y is [None, 10] as we will be using it for an undefined
# number of label outputs, with 10 possible classes
Y = tf.placeholder("float", [None, n_output])

keep_prob = tf.placeholder(tf.float32)  # used to control the dropout rate

weights = {
    'w1': tf.Variable(tf.truncated_normal([n_input, n_hidden1], stddev=0.1)),
    'w2': tf.Variable(tf.truncated_normal([n_hidden1, n_hidden2], stddev=0.1)),
    'w3': tf.Variable(tf.truncated_normal([n_hidden2, n_hidden3], stddev=0.1)),
    'out': tf.Variable(tf.truncated_normal([n_hidden3, n_output], stddev=0.1)),
}

biases = {
    'b1': tf.Variable(tf.constant(0.1, shape=[n_hidden1])),
    'b2': tf.Variable(tf.constant(0.1, shape=[n_hidden2])),
    'b3': tf.Variable(tf.constant(0.1, shape=[n_hidden3])),
    'out': tf.Variable(tf.constant(0.1, shape=[n_output]))
}

layer_1 = tf.add(tf.matmul(X, weights['w1']), biases['b1'])
layer_2 = tf.add(tf.matmul(layer_1, weights['w2']), biases['b2'])
layer_3 = tf.add(tf.matmul(layer_2, weights['w3']), biases['b3'])
layer_drop = tf.nn.dropout(layer_3, keep_prob)
output_layer = tf.matmul(layer_3, weights['out']) + biases['out']



cross_entropy = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(
        labels=Y, logits=output_layer
        ))

# The Adam optimizer extends upon gradient descent optimization by
# using momentum to speed up the process through computing an exponentially
# weighted average of the gradients and using that in the adjustments
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)


###############################
#####Training and Testing######
###############################

# In correct_pred, we use the arg_max function to compare which images
# are being predicted correctly by looking at the output_layer (predictions)
# and Y (labels), and we use the equal function to return this as a list of Booleans.
correct_pred = tf.equal(tf.argmax(output_layer, 1), tf.argmax(Y, 1))

# then cast this list to floats and calculate the mean to get a total accuracy score.
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

# initialize a session for running the graph.
# feed the network with our training examples, and once trained, we feed the same
# graph with new test examples to determine the accuracy of the model
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

# train on mini batches
for i in range(n_iterations):
    batch_x, batch_y = mnist.train.next_batch(batch_size)
    sess.run(train_step, feed_dict={
        X: batch_x, Y: batch_y, keep_prob: dropout
        })

    # print loss and accuracy (per minibatch)
    if i % 100 == 0:
        minibatch_loss, minibatch_accuracy = sess.run(
            [cross_entropy, accuracy],
            feed_dict={X: batch_x, Y: batch_y, keep_prob: 1.0}
            )
        print(
            "Iteration",
            str(i),
            "\t| Loss =",
            str(minibatch_loss),
            "\t| Accuracy =",
            str(minibatch_accuracy)
            )

# run the session on the test images
test_accuracy = sess.run(accuracy, feed_dict={X: mnist.test.images, Y: mnist.test.labels, keep_prob: 1.0})
print("\nAccuracy on test set:", test_accuracy)

#load the test image of the handwritten digit:
# Note: image file must be 28x28 pixels
for i in range(1,10):
    img = np.invert(Image.open("test_images/test" + str(i) + ".png").convert('L')).ravel()
    prediction = sess.run(tf.argmax(output_layer, 1), feed_dict={X: [img]})
    print ("Prediction for test image" + str(i) + ":", np.squeeze(prediction))