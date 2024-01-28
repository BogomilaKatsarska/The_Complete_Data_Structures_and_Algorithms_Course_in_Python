'''
Given a directed graph and two nodes (S and E), design an algorithm to find out whether there is a route from S to E.
'''


class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def checkRoute(self, startNode, endNode):
        visited = [startNode]
        queue = [startNode]
        path = False
        while queue:
            dequeued_verted = queue.pop(0)
            for adjancent_vertex in self.gdict[dequeued_verted]:
                if adjancent_vertex not in visited:
                    if adjancent_vertex == endNode:
                        path = True
                        break
                    else:
                        visited.append(adjancent_vertex)
                        queue.append(adjancent_vertex)
        return path

customDict = {"a": ["c", "d", "b"],
                "b": ["j"],
                "c": ["g"],
                "d": [],
                "e": ["f", "a"],
                "f": ["i"],
                "g": ["d", "h"],
                "h": [],
                "i": [],
                "j": []
                }

g = Graph(customDict)
print(g.checkRoute("a", "j"))  # True
print(g.checkRoute("a", "e"))  # False