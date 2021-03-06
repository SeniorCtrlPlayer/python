#coding:utf-8
#预测多或预测少的影响一样
#0导入模块,生成模拟数据集
import tensorflow as tf
import numpy as np
BATCH_SIZE = 8
seed = 23455

#基于seed产生随机数
rdm = np.random.RandomState(seed)
#随机数返回32行2列的矩阵 表示32组 体积和重量 作为输入数据集
X = rdm.rand(32,2)
#从X这个32行2列的矩阵中 取出一行 判读如果和小于1 给Y复赋值1 如果和不小于1 给Y赋值0
#作为输入数据集的标签（正确答案）
Y_ = [[x1+x2+(rdm.rand()/10.0-0.05)] for (x1,x2) in X]

#1定义神经网络的输入、参数和输出，定义前向传播过程。
#x,y_为占位
x = tf.placeholder(tf.float32,shape=(None,2))
y_= tf.placeholder(tf.float32,shape=(None,1))

w1=tf.Variable(tf.random_normal([2,1],stddev=1,seed=1))
y =tf.matmul(x,w1)

#定义损失函数及反向传播方法。
#定义损失函数为MSE,反向传播方法为梯度下降。
loss=tf.reduce_mean(tf.square(y-y_))
train_step=tf.train.GradientDescentOptimizer(0.001).minimize(loss)

#3生成会话,训练steps轮
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    #训练模型
    STEPS = 20000
    for i in range(STEPS):
        start = (i*BATCH_SIZE) % 32
        end = start + BATCH_SIZE
        sess.run(train_step,feed_dict={x:X[start:end],y_:Y_[start:end]})
        if i % 500 == 0:
            total_loss = sess.run(loss,feed_dict={x:X,y_:Y_})
            print("After %d training step(s), loss on all data is %g"%(i,total_loss))
            print("w1 is: ")
            print(sess.run(w1),"\n")
    print("Final w1 is: \n",sess.run(w1))
