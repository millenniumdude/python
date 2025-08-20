'''Adjacency Matrix Implementation of Graph

Write a class Graph to implement adjacency matrix representation of a simple and undirected graph.'''

class GraphMatrix:

#In class Graph, define __init__ method to initialise vertex_count and adj_matrix.

    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.adj_matrix = [[0 for i in range(vertex_count)] for j in range(vertex_count)]

#In class Graph, define add_edge() method to add an edge in the graph with given weight.

    def add_edge(self, u, v, weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
        else:
            print("Invalid Vertex")
            
#In class Graph, define remove_edge() method to remove an edge from the graph.

    def remove_edge(self, u, v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v] = 0
            self.adj_matrix[v][u] = 0
        else:
            print("Invalid Vertex")

#In class Graph, define has_edge() method to check whether two given vertices are connected by an edge or not.

    def has_edge(self, u, v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return self.adj_matrix[u][v] != 0
        else:
            print("Invalid Vertex")

#In class Graph, define print_adj_matrix() method to print adjacency matrix.
        
    def print_adj_matrix(self):
        for row in self.adj_matrix:
            print(" ".join(map(str,row)))


'''Adjacency List Implementation of Graph
Write a class Graph to implement list representation of a graph data structure.'''

class GraphList:

#In class Graph, define __init__() method to initialise instance object variables vertex_count and a dict adj_list where key is vertex number and value is a list of adjacent vertices.

    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.adj_list = {i: [] for i in range(vertex_count)}

#In class Graph, define add_edge() method to add an edge in the graph with given vertices and weight.

    def add_edge(self, u, v, weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u].append((v, weight))
            self.adj_list[v].append((u, weight))
        else:
            print("Invalid Vertex")  

#In class Graph, define remove_edge() method to remove an edge from the graph.

    def remove_edge(self, u, v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u] = [(node, w) for node, w in self.adj_list[u] if node != v]
            self.adj_list[v] = [(node, w) for node, w in self.adj_list[v] if node != u]
        else:
            print("Invalid Vertex")

#In class Graph, define has_edge() method to check whether an edge exists or not for a given pair of vertices.

    def has_edge(self, u, v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return any(node == v for node, _ in self.adj_list[u])
        else:
            print("Invalid Vertex")

#In class Graph, define print_adj_list() method to print adjacency lists of graph.

    def print_adj_list(self):
        for key in self.adj_list:
            print(f"{key} -> {self.adj_list[key]}")


gl = GraphList(4)
gl.add_edge(0, 1, 1)
gl.add_edge(1, 2, 2)
gl.add_edge(2, 3, 3)

gm = GraphMatrix(4)
gm.add_edge(0, 1, 1)
gm.add_edge(1, 2, 2)
gm.add_edge(2, 3, 3)

gm.print_adj_matrix()
gl.print_adj_list()

print("Edge (1,2):", gl.has_edge(1, 2))
print("Edge (1,2):", gm.has_edge(1, 2))

#gm.remove_edge(1, 2)
#gm.print_adj_list()

#gl.remove_edge(1, 2)
#gl.print_adj_list()
