'''
1.Minimum Spanning Tree: MST is a subset of the edges of connected, unweighted and undirected graph, which:
    - connects al vertices together
    - no cycle
    - minimum total edge
2.Disjoint Set: a data structure that keeps track of set of elements which are partitionted in a number of
    disjoint and non overlapping sets and each sets have representative which helps in identifying the sets
        - Make set(N) - usd to create initial set
        - Union set(x,y) - merge two given sets
        - Find Set(B)
'''


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


