import pandas as pd, math, numpy as np

data = pd.read_csv("id3.csv")
feat = [i for i in data]
feat.remove("answer")

class node:

    def __init__(self):
        self.child = []
        self.value = ""
        self.isLeaf = False
        self.pred = ""

def entropy(ex):
    p, n = 0.0, 0.0

    for _,row in ex.iterrows():
        if row["answer"] == "yes":
            p += 1
        else:
            n += 1
    
    if p == 0.0 or n == 0.0:
        return 0.0
    else:
        P = p/(p+n)
        N = n/(p+n)
        return -(P*math.log(P,2) + N*math.log(N,2))

def infoGain(ex, attr):
    unique = np.unique(ex[attr])
    gain = entropy(ex)

    for i in unique:
        subdata = ex[ex[attr] == i]
        subEntropy = entropy(subdata)
        gain -= float(len(subdata)) / float(len(ex)) * subEntropy

    return gain

def id3(ex, attr):
    root = node()
    maxGain, maxFeat = 0, ""

    for f in attr:
        gain = infoGain(ex, f)
        if gain > maxGain: 
            maxGain, maxFeat = gain, f
  
    root.value = maxFeat
    unique = np.unique(ex[maxFeat])

    for i in unique:
        subData = ex[ex[maxFeat] == i]
        if entropy(subData) == 0.0:
            new = node()
            new.isLeaf = True
            new.value = i
            new.pred = np.unique(subData["answer"])
            root.child.append(new)
        else:
            dummy = node()
            dummy.value = i
            newAttr = attr.copy()
            newAttr.remove(maxFeat)
            child = id3(subData, newAttr)
            dummy.child.append(child)
            root.child.append(dummy)

    return root

def display(root: node, d=0):
    for i in range(d):
        print("\t", end="")
    print(root.value, end="")

    if root.isLeaf:
        print(" -> ", root.pred)
    
    for child in root.child:
        display(child, d+1)

root = id3(data, feat)
display(root)