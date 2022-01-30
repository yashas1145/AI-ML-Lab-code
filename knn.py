from sklearn.model_selection import train_test_split as tts
from sklearn.neighbors import KNeighborsClassifier as knc
from sklearn.metrics import classification_report as cr, confusion_matrix as cm
from sklearn import datasets as dt

iris = dt.load_iris()
data, label = iris.data, iris.target

xTr, xT, yTr, yT = tts(data, label, test_size=0.30)
kmc = knc(5)
kmc.fit(xTr, yTr)
yPr = kmc.predict(xT)

print(cm(yT, yPr))
print(cr(yT, yPr))
