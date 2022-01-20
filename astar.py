graph = {'A':[('C', 1)], 'B':[('C', 2)], 'C':[('G', 3)], 'S':[('A', 1), ('B', 1)]}  #Declare a graph as a dictionary. Format: { Node : (Neighbor, Weight) }

def getNeighbor(node):  #Return neighbors of a node as a list
    if node in graph:
        return graph[node]
    else:
        return None
    
def astar(start, stop): #A Star implementation

    open = set(start)   #Open set
    close = set()       #Close set
    dist, parent = {}, {}   #Distance and parent dictionaries to maintain track of nodes
    hv = {'A': 4, 'B': 1, 'C': 1, 'S': 2, 'G': 0}   #Heuristic values of all nodes

    dist[start] = 0         #Starting node distance is 0
    parent[start] = start   #Parent of starting node is itself

    while len(open) > 0:    #For all nodes in open set
        n = None            #Take a temp node n

        for v in open:      #Check for lowest cost of a node in open set and assign it to temp node n
            if n == None or dist[v] + hv[v] < dist[n] + hv[n]:
                n = v
        
        if n == stop or graph[n] == None:   #If n is the destination or n has no neighbors, do nothing
            pass

        else:
            for (m, weight) in getNeighbor(n):  #For all neighbors of n

                if m not in open and m not in close:    #If the neighbor 'm' is not in open set and close set
                    open.add(m)                             #Add m to open set
                    parent[m] = n                           #Assign parent of m as n
                    dist[m] = dist[n] +  weight              #Calculate distance of m from n

                else:                                   #If m is already in open set
                    if dist[m] > dist[n] + weight:          #Compare previous distance of m
                        dist[m] = dist[n] + weight          #Update only if greater
                        parent[m] = n                       #Assign parent of m as n
                    
                        if m in close:                  #If m is already in close set
                            close.remove(m)                 #Remove m from close set
                            open.add(m)                     #Add m to close set

        if n == None:   #If there is no neighbor for n                              
            print("No path found")
            return None

        if n == stop:   #If n is the sop node
            path = []   #Declare a path list

            while parent[n] != n:   #While parent of n is not itself
                path.append(n)      #Append all parents of n
                n = parent[n]       #Update the node n

            path.append(start)      #Append start to path
            print("Path found: {}".format(path[::-1]))  #Print reverse of path to get output
            return path
        
        open.remove(n)  #Remove n from open
        close.add(n)    #Add n to close

    print("No path found")  #404
    return None

astar('S', 'G')