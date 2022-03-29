import pandas as pd, numpy as np, matplotlib.pyplot as plt

def kernel(p, x, k):
    m, n = np.shape(x)
    w = np.mat(np.eye((m)))
    for i in range(m):
        d = p - X[i]
        w[i,i] = np.exp(-(d*d.T)/(2.0*k**2))
    return w

def localWeight(p, x, y, k):
    w = kernel(p, x, k)
    W = (X.T * (w*X)).I * (X.T * (w*y.T))
    return W

def lwr(x, y, k):
    m, n = np.shape(x)
    yPr = np.zeros(m)
    for i in range(m):
        yPr[i] = x[i] * localWeight(x[i], x, y, k)
    return yPr

def graph(x, y):
    si = X[:,1].argsort(0)
    xs = X[si][:,0]
    plt.subplot(1,1,1)
    plt.scatter(np.array(data.bill), np.array(data.tip))
    plt.plot(xs[:,1], Y[si], color='red')
    plt.show()

data = pd.read_csv('regression.csv')
mBill, mTip = np.mat(np.array(data.bill)), np.mat(np.array(data.tip))
one = np.mat(np.ones(np.shape(mBill)[1]))
X = np.hstack((one.T, mBill.T))
Y = lwr(X, mTip, 3)
graph(X, Y)
