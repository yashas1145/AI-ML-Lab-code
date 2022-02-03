from re import X
import matplotlib.pyplot as plt, pandas as pd, numpy as np

def kernel(p, x, k):
    m, n = np.shape(x)
    w = np.mat(np.eye((m)))

    for j in range(m):
        d = p - X[j]
        w[j,j] = np.exp(d * d.T/(-2.0*k**2))
    return w

def localWeight(p, x, y, k):
    w = kernel(p, x, k)
    W = (X.T*(w*X)).I * (X.T*(w*y.T))
    return W

def lwr(x, y, k):
    m, n = np.shape(x)
    yPr = np.zeros(m)
    for i in range(m):
        yPr[i] = x[i] * localWeight(x[i], x, y, k)
    return yPr

def graphPlot(x, yPr):
    sortIndex = X[:,1].argsort(0)
    xSort = X[sortIndex][:,0]
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.scatter(bill, tip, color="green")
    ax.plot(xSort[:,1], yPr[sortIndex], color="red", linewidth=3)
    plt.xlabel("Total bill")
    plt.ylabel("Tip")
    plt.show()

data = pd.read_csv("regression.csv")
bill, tip = np.array(data.total_bill), np.array(data.tip)
mBill, mTip = np.mat(bill), np.mat(tip)
m = np.shape(mBill)[1]
one = np.mat(np.ones(m))
X = np.hstack((one.T, mBill.T))
yPr = lwr(X, mTip, 3)
graphPlot(X, yPr)
