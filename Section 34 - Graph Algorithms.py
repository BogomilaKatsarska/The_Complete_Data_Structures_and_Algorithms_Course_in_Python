'''
1.Graph: consists of finite set of VERTICES(or nodes) and a set of EDGES which connect a pair of nodes
    - Vertices: vertices are the nodes of the graph
    - Edge: the edge is the line that connects pairs of vertices
    - Unweighted graph: a graph which does not have a weight associated with any edge
    - Weighted graph: a graph which has a weight associated with any edge
    - Undirected graph: in case the edges of the graph do not have a direction associated with them
    - Directed graph: if the edges in a graph have a direction associated with them
    - Cyclic graph: a graph which has at least one loop
    - Acyclic graph: a graph with no loop
    - Tree: a special case of directed acyclic graphs

2.Types of Graphs:
    - Directed
        - Weighted
            - Negative
            - Positive
        - Unweighted
    - Undirected
        - Weighted
            - Negative
            - Positive
        - Unweighted

3. Graph Representation:
    - Adjacency Matrix: an adjacency matrix is a square matrix(or you can say it 2D array). The elements of the matrix
    indicate whether pairs of vertices are adjacent or not in the graph
    - If the graph is complete or almost complete we should use adjacency matrix

        A   B   C   D   E
    A   0   1   1   1   0
    B   1   0   0   0   1
    C   1   0   0   1   0
    D   1   0   1   0   1
    E   0   1   0   1   0

    - Adjacency List: an adjacency list is collection of unordered list used to represent a graph. Each list describes
    the set of neighbors of vertex in the graph. (via linked list)
    - If the number of edges are few we should use adjacency list

    A -> B -> C -> D
    B -> A -> E
    C -> A -> D
    D -> A -> C -> E
    E -> B -> D

    - Python dictionary implementation
    { A: [B,C,D],
      B: [A,D],
      C: [A,D]...}
'''


class Graph:
    def __init__(self, adjacency_list=None):
        if adjacency_list is None:
            adjacency_list = {}
        self.adjacency_list = adjacency_list

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ':', self.adjacency_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
            except ValueError:
                'The edge cannot be removed'
            return True
        return False

    def bfs(self, vertex): #Time Complexity: O(V+E) Space Complexity:O(V)
        visited = set()
        visited.add(vertex)
        queue = dequeue([vertex])
        while queue:
            current_vertex = queue.popleft
            print(current_vertex)
            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    queue.append(adjacent_vertex)

    def dfs(self, vertex): #Time Complexity: O(V+E)
        visited = set()
        stack = [vertex]
        while stack:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if adjacent_vertex not in visited:
                    stack.append(adjacent_vertex)
