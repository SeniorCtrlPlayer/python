#搭建graph计算图
import tensorflow as tf
x=tf.constant([[1.0,2.0]])
w=tf.constant([[3.0],[4.0]])
y=tf.matmul(x,w)
print(y)
#绘画，执行计算图中的节点运算
with tf.Session() as sess:
    print(sess.run(y))
