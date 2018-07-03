import tensorflow as tf
# hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
# print(sess.run(hello))

#define 2*2 matrix for matrix1, matrix2, matrix3
matrix1 = tf.constant([1,2,3,4], name= "matrix1", shape =[2,2])

matrix2 = tf.constant([1,4,3,4], name= "matrix2", shape =[2,2])

matrix3 = tf.constant([1,8,2,11], name= "matrix3", shape =[2,2])


#power of a matrix
power = tf.pow(matrix1,2)

#sum of 2 matrices
sum = tf.add(power,matrix2)

#multiplication of 2 matrices
total = tf.matmul(sum,matrix3)


print(sess.run(total))