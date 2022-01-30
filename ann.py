import numpy as np

x = np.array(([2,9], [1,5], [3,6]), dtype=float)
y = np.array(([94], [85], [67]), dtype=float)

x = x / np.amax(x, axis=0)
y = y / 100

epochs, lr, i, h, o = 7000, 0.1, 2, 3, 1
wh, bh = np.random.uniform(size=(i, h)), np.random.uniform(size=(1, h))
wo, bo = np.random.uniform(size=(h, o)), np.random.uniform(size=(1, o))

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def dersig(x):
    return x * (1-x)

for i in range(epochs):
    hl = sigmoid(np.dot(x, wh) + bh)        #Hidden layer
    ol = sigmoid(np.dot(hl, wo) + bo)       #Output layer
    derOl = (y-ol) * dersig(ol)             #Derivative of output layer
    derHl = derOl.dot(wo.T) * dersig(hl)    #Derivative of hidden layer
    wo += hl.T.dot(derOl) * lr              #Weight adjustment of output layer
    wh += x.T.dot(derHl) * lr               #Weight adjustment of hidden layer

print(str(x))
print(str(y))
print(ol)
