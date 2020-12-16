import mxnet as mx
from mxnet import gluon

num_hidden = 64
net = gluon.nn.HybridSequential()
with net.name_scope():
    net.add(gluon.nn.Dense(num_hidden, activation="relu"))
    net.add(gluon.nn.Dense(num_hidden, activation="relu"))
    net.add(gluon.nn.Dense(10))

# 绘制逻辑
net.hybridize()
net.collect_params().initialize()
x = mx.sym.var('data')
sym = net(x)
mx.viz.plot_network(sym)