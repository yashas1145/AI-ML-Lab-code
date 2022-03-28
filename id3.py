import pandas as pd, numpy as np, math

data = pd.read_csv("id3.csv")
feat = [i for i in data]
feat.remove('answer')

class node:
    def __init__(self):
        self.child, self.isLeaf, self.value, self.pred = [], False, '', ''

def entropy(x):
    p, n = 0.0, 0.0
    for _,i in x.iterrows():
        if i['answer'] == 'yes':
            p += 1
        else:
            n += 1

    if p == 0.0 or n == 0.0:
        return 0.0

    P, N = (p/(p+n)), (n/(p+n))
    return -(P*math.log(P,2) + N*math.log(N,2))

def infoGain(x, attr):
    unique = np.unique(x[attr])
    gain = entropy(x)
    for i in unique:
        sData = x[x[attr] == i]
        sEntro = entropy(sData)
        gain -= float(len(sData))/float(len(x)) * sEntro

    return gain

def display(root:node, d=0):
    for i in range(d):
        print("\t", end="")
    print(root.value, end="")

    if root.isLeaf:
        print("->", root.pred)

    for child in root.child:
        display(child, d+1)

def id3(x, attr):
    root, maxGain, maxFeat = node(), 0, ''
    for feat in attr:
        gain = infoGain(x, feat)
        if gain > maxGain:
            maxGain, maxFeat = gain, feat

    root.value = maxFeat
    unique = np.unique(x[maxFeat])

    for i in unique:
        sData = x[x[maxFeat] == i]
        if entropy(sData) == 0.0:
            new = node()
            new.isLeaf, new.value, new.pred = True, i, np.unique(sData['answer'])
            root.child.append(new)
        else:
            new = node()
            new.value = i
            newAttr = attr.copy()
            newAttr.remove(maxFeat)
            child = id3(sData, newAttr)
            new.child.append(child)
            root.child.append(new)

    return root

display(id3(data, feat))
