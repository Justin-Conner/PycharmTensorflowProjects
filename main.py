import tensorflow as tf

# initialization of tensors
# x = tf.constant(4, shape=(1,1), dtype=tf.float32)
# x = tf.constant([[1,2,3],[4,5,6]])
# x = tf.ones((3,3))
# x = tf.random.normal((3,3), mean=0, stddev=1) # standard distribution
# x = tf.random.uniform((1,3), minval=0, maxval=1) # uniform distribution
# x = tf.range(start=1, limit=10, delta=2)

# print(x)
# mathematical operations

# x = tf.constant ([1,2,3])
# y = tf.constant([9,8,7])
# z = tf.add(x,y)
# create a dot product
# z = tf.tensordot(x,y, axes=1)
# exponentiation
# z= x ** 5
# matrix multiplication
# x = tf.random.normal((2,3 ))
# y = tf.random.normal((3,4 ))
# z = tf.matmul(x,y)
# print(z)

# indexing

# x = tf.constant([0,1,1,2,3,1,2,3])
# print(x[:])

# exclude the first indexed elemenmt
# print(x[1:])
# a range of indexed elements
# print(x[1:3])
# results "tf.Tensor([1 1], shape=(2,), dtype=int32)"

# skip every other value
# print(x[::2])
# results "tf.Tensor([0 1 3 2], shape=(4,), dtype=int32)"

# reverse the order
# print (x[::-1])
# results "tf.Tensor([3 2 1 3 2 1 1 0], shape=(8,), dtype=int32)"

# Reshaping

x = tf.range(9)
print (x)
# results tf.Tensor([0 1 2 3 4 5 6 7 8], shape=(9,), dtype=int32)
x = tf.reshape(x, (3,3))
print(x)
# results tf.Tensor(
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]], shape=(3, 3), dtype=int32)






