'''
1.Kruskal's Algorithm:
    - It is a greedy algorithm
    - Finds a minimum spanning tree for weighted undirected graphs in two ways:
        - Add increasing cost edges at each step
        - Avoid any cycle at each step

2. Prim's Algorithm:
    - It is a greedy algorithm
    - It finds a minimum spanning tree for weighted undirected graphs in following ways:
        - Take any vertex as a source, set its weight to 0 and all other vertices to infinity
        - For every adjacent vertices if the current weight is more than the current edge then we set it to current edge
        - Then we mark current vertex as visited
        - Repeat these steps for all vertices in increasing order of weight
'''
import sys

class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[xroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1


class Graph:
    def __init__(self, vertices):
        self.v = vertices #number of vertices
        self.graph = []
        self.nodes = []
        self.MST = []

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    def add_node(self, value):
        self.nodes.append(value)

    def print_solution(self, s, d, w):
        for s, d, w in self.MST:
            print(f"{s} - {d}: {w}")

    def kruskal_algorithm(self):
        i, e = 0, 0
        ds = DisjointSet(self.nodes)
        self.graph = sorted(self.graph, key=lambda item: item[2])
        while e < self.v - 1:
            s, d, w = self.graph[i]
            i += 1
            x = ds.find(s)
            y = ds.find(d)
            if x != y:
                e += 1
                self.MST.append([s, d, w])
                ds.union(x, y)
        self.print_solution(s,d,w)


class GraphForPrims:
    def __init__(self, vertex_num, edges, nodes):
        self.edges = edges
        self.nodes = nodes
        self.vertex_num = vertex_num
        self.MST = []

    def print_solution(self):
        print("Edge: Weight")
        for s, d, w in self.MST:
            print(f"{s} -> {d} : {w}")

    def prims_algorithm(self):
        visited = [0]*self.vertex_num
        edge_num = 0
        visited[0] = True
        while edge_num < self.vertex_num -1:
            min = sys.maxsize
            for i in range(self.vertex_num):
                if visited[i]:
                    for j in range(self.vertex_num):
                        if not visited[j] and self.edges[i][j]:
                            if min > self.edges[i][j]:
                                min = self.edges[i][j]
                                s = i
                                d = j
            self.MST.append([self.nodes[s], self.nodes[d], self.edges[s][d]])
            visited[d] = True
            edge_num += 1
        self.print_solution()