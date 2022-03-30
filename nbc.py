import random, csv, math as m

def loadcsv(file):
    data = list(csv.reader(open(file, 'r')))
    for i in range(len(data)):
        data[i] = [float(j) for j in data[i]]
    return data

def splitdata(data, sr):
    trainset, trainsize, copy = [], int(len(data)*sr), list(data)
    while len(trainset) < trainsize:
        index = random.randrange(len(copy))
        trainset.append(copy.pop(index))
    return trainset, copy

def splitclass(data):
    s = {}
    for i in range(len(data)):
        v = data[i]
        if v[-1] not in s:
            s[v[-1]] = []
        s[v[-1]].append(v)
    return s

def mean(n):
    return sum(n)/float(len(n))

def stdev(n):
    a = mean(n)
    v = sum([(x-a)**2 for x in n])/float(len(n)-1)
    return m.sqrt(v)

def summary(data):
    s = [(mean(i), stdev(i)) for i in zip(*data)]
    del s[-1]
    return s

def summaryclass(data):
    sep = splitclass(data)
    s = {}
    for i, j in sep.items():
        s[i] = summary(j)
    return s

def probability(x, a, s):
    x = m.exp((x-a)**2/(2*s**2))
    return s * x * (1/m.sqrt(2*m.pi))

def probabilityclass(s, v):
    p = {}
    for i, j in s.items():
        p[i] = 1
        for k in range(len(j)):
            mean, stdev = j[k]
            x = v[k]
            p[i] *= probability(x, mean, stdev)

        return p

def predict(s, v):
    p = probabilityclass(s, v)
    bl, bp = None, -1
    for i, j in p.items():
        if bl is None or j > bp:
            bl, bp = i, j
    return bl

def getprediction(s, t):
    p = []
    for i in range(len(t)):
        p.append(predict(s, t[i]))
    return p

def getaccuracy(t, p):
    c = 0
    for i in range(len(t)):
        if t[i][-1] == p[i]:
            c += 1
    return c * 100.0 / float(len(t))

data = loadcsv('nbc.csv')
train, test = splitdata(data, 0.67)
print("Total: {} Train: {} Test: {}".format(len(data), len(train), len(test)))
s = summaryclass(train)
p = getprediction(s, test)
a = getaccuracy(test, p)
print("Accuracy: {}".format(a))
