class graph:

    def __init__(self, graph, hvList, start):
        self.g = graph
        self.h = hvList
        self.start = start

        self.parent, self.status, self.soln = {}, {}, {}

    def applyAoStar(self):
        self.aoStar(self.start, False)

    def getNeighbor(self, node):
        return self.g.get(node, '')

    def getStatus(self, node):
        return self.status.get(node, 0)

    def setStatus(self, node, status):
        self.status[node] = status

    def gethv(self, node):
        return self.h.get(node, 0)

    def sethv(self, node, hv):
        self.h[node] = hv

    def printSolution(self):
        print("Traverse the graph from {} node".format(self.start))
        print(self.soln)

    def computeCost(self, node):
        minCost, costToChild = 0, {}
        costToChild[minCost] = []
        flag = True

        for nodeTuple in self.getNeighbor(node):
            cost, nodeList = 0, []

            for m, weight in nodeTuple:
                cost += self.gethv(m) + weight
                nodeList.append(m)
            
            if flag == True:
                minCost = cost
                costToChild[minCost] = nodeList
                flag = False
            else:
                if minCost > cost:
                    minCost = cost
                    costToChild[minCost] = nodeList
        
        return minCost, costToChild[minCost]

    def aoStar(self, node, bt):
        print("Heuristic values: ", self.h)
        print("Solution graph: ", self.soln)
        print("Processing node: ", node)
        print("-"*30)

        if self.getStatus(node) >= 0:
            minCost, chilNodeList = self.computeCost(node)
            self.sethv(node, minCost)
            self.setStatus(node, len(chilNodeList))

            solved = True
            for child in chilNodeList:
                self.parent[child] = node
                if self.getStatus(child) != -1: solved = False
            
            if solved == True:
                self.setStatus(node, -1)
                self.soln[node] = chilNodeList

            if node != self.start:
                self.aoStar(self.parent[node], True)

            if bt == False:
                for child in chilNodeList:
                    self.setStatus(child, 0)
                    self.aoStar(child, False)

hv = {'A': 1, 'B': 6, 'C': 2, 'D': 12, 'E': 2, 'F': 1, 'G': 5, 'H': 7, 'I': 7, 'J': 1}
g1 = {'A': [[('B', 1), ('C', 1)], [('D', 1)]], 'B': [[('G', 1)], [('H', 1)]], 'C': [[('J', 1)]], 'D': [[('E', 1), ('F', 1)]], 'G': [[('I', 1)]]}

ao = graph(g1, hv, 'A')
ao.applyAoStar()
ao.printSolution()