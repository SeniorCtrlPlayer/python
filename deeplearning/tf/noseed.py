#coding:utf-8
#两层简单神经网络(全连接)
import tensorflow as tf

#定义输入和参数
x=tf.constant([[0.7,0.5]])
#不设置随机种子，值为随机出现
w1=tf.Variable(tf.random_normal([2,3],stddev=1))
w2=tf.Variable(tf.random_normal([3,1],stddev=1))

#定义前向传播过程
a=tf.matmul(x,w1)
y=tf.matmul(a,w2)

#用会话计算结果
with tf.Session() as sess:
    #对所有变量进行初始化
    init_op=tf.global_variables_initializer()
    sess.run(init_op)

    print("w1 in tf3_3.py is: ",sess.run(w1))
    print("w2 in tf3_3.py is: ",sess.run(w2))
    print("a in tf3_3.py is: ",sess.run(a))
    print("y in tf3_3.py is: ",sess.run(y))
'''
y in tf3_3.py is:
[[3.0904665]]
'''
