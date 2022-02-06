import csv, random, math

def loadcsv(file):
    line = csv.reader(open(file, "r"))
    data = list(line)
    for i in range(len(data)):
        data[i] = [float(x) for x in data[i]]
    return data

def splitData(data, splitRatio):
    trainSize, trainSet = int(len(data) * splitRatio), []
    copy = list(data)
    
    while len(trainSet) < trainSize:
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))
    return [trainSet, copy]

def splitClass(data):
    seperate = {}
    for i in range(len(data)):
        vector = data[i]
        if vector[-1] not in seperate:
            seperate[vector[-1]] = []
        seperate[vector[-1]].append(vector)
    return seperate

def mean(number):
    return sum(number)/float(len(number))

def stdev(number):
    avg = mean(number)
    variance = sum([pow(x-avg, 2) for x in number])/float(len(number)-1)
    return math.sqrt(variance)

def summarize(data):
    summary = [(mean(attr), stdev(attr)) for attr in zip(*data)]
    del summary[-1]
    return summary

def summarizeByClass(data):
    seperate = splitClass(data)
    summary = {}
    for classValue, instance in seperate.items():
        summary[classValue] = summarize(instance)
    return summary

def calculateProbability(x, mean, stdev):
    exp = math.exp(-(math.pow(x-mean, 2)/(2*math.pow(stdev,2))))
    return (1/(math.sqrt(2*math.pi) * stdev)) * exp

def calculateClassProbability(summary, vector):
    prob = {}
    for classValue, classSummary in summary.items():
        prob[classValue] = 1
        for i in range(len(classSummary)):
            mean, stdev = classSummary[i]
            x = vector[i]
            prob[classValue] *= calculateProbability(x, mean, stdev)
        return prob

def predict(summary, vector):
    prob = calculateClassProbability(summary, vector)
    bestLabel, bestProb = None, -1
    for classValue, prob in prob.items():
        if bestLabel is None or prob > bestProb:
            bestProb = prob
            bestLabel = classValue
    return bestLabel

def getPrediction(summary, test):
    pred = []
    for i in range(len(test)):
        result = predict(summary, test[i])
        pred.append(result)
    return pred

def getAccuracy(test, pred):
    correct = 0
    for i in range(len(test)):
        if test[i][-1] == pred[i]:
            correct += 1
    return (correct/float(len(test))) * 100.0

def main():
    data = loadcsv("nbc.csv")
    trainSet, testSet = splitData(data, 0.67)
    print("Split {} rows into train {} and test {} rows".format(len(data), len(trainSet), len(testSet)))
    summary = summarizeByClass(trainSet)
    pred = getPrediction(summary, testSet)
    accuracy = getAccuracy(testSet, pred)
    print("Accuracy of the classifier is: {}".format(accuracy))

if __name__ == "__main__":
    main()
