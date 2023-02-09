class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph=[]
    def add_edges(self,s,d,w):
        self.graph.append([s,d,w])
    def print_solution(self,dist):
        print("The shortest distance from source to vertex is ")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i,dist[i]))
    def bellman_ford(self,src):
        dist = [float("Inf")] * self.V
        dist[src] = 0
        for _ in range(self.V - 1):
            for s,d,w in self.graph:
                if dist[s] != float("Inf") and dist[s]+w < dist[d]:
                    dist[d] = dist[s]+w
        for s,d,w in self.graph:
            if dist[s] != float("Inf") and dist[s]+w < dist[d]:
                print("Negative Cycle exist")
        self.print_solution(dist)
g = Graph(5)
g.add_edges(0,1,5)
g.add_edges(0,2,4)
g.add_edges(1,3,3)
g.add_edges(2,1,6)
g.add_edges(3,2,2)
g.bellman_ford(0)