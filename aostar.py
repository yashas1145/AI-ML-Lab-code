class graph:
    def __init__(self, start):
        self.g = {'A': [[('B', 1), ('C', 1)], [('D', 1)]], 'B': [[('G', 1)], [('H', 1)]], 'C': [[('J', 1)]], 'D': [[('E', 1), ('F', 1)]], 'G': [[('I', 1)]]}
        self.h = {'A': 1, 'B': 6, 'C': 2, 'D': 12, 'E': 2, 'F': 1, 'G': 5, 'H': 7, 'I': 7, 'J': 1}
        self.start, self.status, self.parent, self.soln = start, {}, {}, {}

    def applyaostar(self):
        self.aostar(self.start, False)

    def getNeighbor(self, n):
        return self.g.get(n, '')

    def gethv(self, n):
        return self.h.get(n, 0)

    def getstatus(self, n):
        return self.status.get(n, 0)

    def sethv(self, n, v):
        self.h[n] = v

    def setstatus(self, n, v):
        self.status[n] = v

    def display(self):
        print("Start from {}".format(self.start))
        print(self.soln)

    def cost(self, n):
        mc, childCost = 0, {}   #mc: Minimum cost
        childCost[mc] = []
        flag = True

        for nTuple in self.getNeighbor(n):
            cost, nList = 0, []
            for m,w in nTuple:
                cost += self.gethv(m) + w
                nList.append(m)

            if flag == True:
                mc = cost
                childCost[mc] = nList
                flag = False

            else:
                if mc > cost:
                    mc = cost
                    childCost[mc] = nList

        return mc, childCost[mc]

    def aostar(self, n, bt):
        print("Heuristic values: {}".format(self.h))
        print("Traversal: {}".format(self.soln))
        print("We are at node {}".format(n))
        print("-"*30)

        if self.getstatus(n) >= 0:
            mc, child = self.cost(n)
            self.setstatus(n, len(child))
            self.sethv(n, mc)
            solve = True

            for c in child:
                self.parent[c] = n
                if self.getstatus(c) != -1:
                    solve = False

            if solve == True:
                self.setstatus(n, -1)
                self.soln[n] = child

            if n != self.start:
                self.aostar(self.parent[n], True)

            if bt == False:
                for c in child:
                    self.setstatus(c, 0)
                    self.aostar(c, False)

ao = graph('A')
ao.applyaostar()
ao.display()
