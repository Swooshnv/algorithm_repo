# Define a graph class with integrated kruskal pathfinder (inputs vertices as initializer and nodes as objects)
class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = []
    
    # add_edge: Create a new edge with its vertices
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
 
    # search: Searches for parents of each node
    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])
    
    def apply_union(self, parent, rank, x, y):
        xroot = self.search(parent, x)
        yroot = self.search(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
 
    def kruskal(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.search(parent, u)
            y = self.search(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("Edge:",u, v,end =" ")
            print("-",weight)
 
 
g = Graph(6)
g.add_edge(0, 1, 8)
g.add_edge(0, 2, 7)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 11)
g.add_edge(2, 3, 6)
g.add_edge(2, 5, 10)
g.add_edge(3, 4, 7)
g.add_edge(1, 5, 9)
g.kruskal()