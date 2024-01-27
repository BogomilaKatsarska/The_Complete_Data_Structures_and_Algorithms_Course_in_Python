'''
1.Bellman Ford Algorithm: used to find single source shortest path problem. If there is a negative cycle it catches it
    and reports its existence
        - If in V-th iteration the weight of vertices have changed, it means that we have negative iteration
        - Why 'V-1' times is run Bellman Ford Algorithm?
            - If any node achieved better distance in previous iteration, then that better distance is used to improve
            distance of other vertices
            - Because the worst case we can have is when the path from source is maximum i.e.:
                - Identify worst case graph that can be given to us
'''


class Graph:
    def __init__(self, vertices):
        self.v = vertices #number of vertices
        self.graph = []
        self.nodes = []

    def add_edge(self, s, d, w): #source, destination and weight
        self.graph.append([s, d, w])

    def add_node(self, value):
        self.nodes.append(value)

    def print_solution(self, dist):
        print('Vertex Distance from Source')
        for key, value in dist.items():
            print(' ' + key, ' :  ', value)

    def bellman_ford(self, src):
        dist = {i: float('Infinity') for i in self.nodes}
        dist[src] = 0

        for _ in range(self.v-1):
            for s, d, w in self.graph:
                if dist[s] != float('Infinity') and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        for s, d, w in self.graph:
            if dist[s] != float('Infinity') and dist[s] + w < dist[d]:
                print('Graph contains negative cycle')

        self.print_solution(dist)