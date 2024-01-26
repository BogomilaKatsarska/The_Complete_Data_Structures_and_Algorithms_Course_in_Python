'''
1.Single Source Shortest Path: a single source problem is about finding a path between a given vertex(called source) to
    all other vertices in such that the total distance between them(source and destination) is minimum.
'''

#TODO: watch again
class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def bfs(self, start, end): # BFS works only with unweighted - undirected graph AND unweighted - directed graph
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacent in self.gdict.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)