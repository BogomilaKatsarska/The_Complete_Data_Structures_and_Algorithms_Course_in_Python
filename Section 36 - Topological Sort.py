'''
1.Topological Sort: sorts given actions in such way what if there is a dependency of one action on another,
    then the dependent action always comes later than its parent action.
    - If a vertex depends on current_vertex, go to that vertex and then come back to the current_vertex, else:
    push current_vertex to stack
'''
from collections import defaultdict


class Graph:
    def __init__(self, number_of_vertices):
        self.graph = defaultdict(list)
        self.number_of_vertices = number_of_vertices

    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topological_sort_util(self, v, visited, stack):
        visited.append(v)

        for i in self.graph[v]:
            if i not in visited:
                self.topological_sort_util(i, visited, stack)

        stack.insert(0, v)

    def topological_sort(self):
        visited = []
        stack = []

        for k in list(self.graph):
            if k not in visited:
                self.topological_sort_util(k, visited, stack)

        print(stack)