'''
1.Breadth First Search (BFS)
2.Depth First Search (DFS)
'''

def bfs(self, vertex): #vetrex = arbitrary vertex
    visited = set()
    visited.add(vertex)
    queue = [vertex]
    while queue:
        current_vertex = queue.pop(0)
        print(current_vertex)
        for adjacent_vertex in self.adjacency_list[current_vertex]:
            if adjacent_vertex not in visited:
                visited.add(adjacent_vertex)
                queue.append(adjacent_vertex)


def dfs(self, vertex):
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