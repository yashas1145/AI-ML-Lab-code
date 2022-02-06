import pandas as pd, numpy as np, matplotlib.pyplot as plt
from pyparsing import col
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.mixture import GaussianMixture

data = load_iris()
X = pd.DataFrame(data.data, columns=['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width'])
y = pd.DataFrame(data.target, columns=['Target'])

plt.figure(figsize=(21, 7))
colormap = np.array(['Red', 'Green', 'Black'])

plt.subplot(1,3,1)
plt.scatter(X.Petal_Length, X.Petal_Width, c=colormap[y.Target], s=40)

model = KMeans(3)
model.fit(X)
yPred = np.choose(model.labels_, [0,1,2]).astype(np.int64)

plt.subplot(1,3,2)
plt.scatter(X.Petal_Length, X.Petal_Width, c=colormap[yPred], s=40)

scaler = preprocessing.StandardScaler()
xsa = scaler.fit_transform(X)
xs = pd.DataFrame(xsa, columns=X.columns)
gmm = GaussianMixture(3)
gmm.fit(xs)
yCluster = gmm.predict(xs)

plt.subplot(1,3,3)
plt.scatter(X.Petal_Length, X.Petal_Width, c=colormap[yCluster], s=40)

plt.show()
