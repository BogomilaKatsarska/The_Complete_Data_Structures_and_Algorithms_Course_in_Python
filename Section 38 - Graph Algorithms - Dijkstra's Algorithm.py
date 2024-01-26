import heapq
class Edge:
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex


class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        #previous node that we come to this node
        self.predecessor = None
        self.neighbors = [] #==children
        self.min_distance = float("inf") #default infinity value

    #LT = less than
    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance

    def add_edge(self, weight, destination_vertex):
        edge = Edge(weight, self, destination_vertex)
        self.neighbors.append(edge)


class Dijkastra:
    def __init__(self):
        self.heap = []

    def calculate(self, start_vertex):
        start_vertex.min_distance = 0
        heapq.heappush(self.heap, start_vertex)
        while self.heap:
            #pop element with the lowest distance
            actual_vertex = heapq.heappop(self.heap)
            if actual_vertex.visited:
                continue
            #consider the neighbors
            for edge in actual_vertex.neighbors:
                start = edge.start_vertex
                target = edge.target_vertex
                new_distance = start.min_distance + edge.weight
                if new_distance < target.min_distance:
                    target.min_distance = new_distance
                    target.predecessor = start
                    #update the heap
                    heapq.heappush(self.heap, target)
                    #[F-19, F-17]
            actual_vertex.visited = True

    def get_shortest_path(self, vertex):
        print(f"The shortest path to the vertex is {vertex.min_distance}")
        actual_vertex = vertex
        while actual_vertex is not None:
            print(actual_vertex.name, end=' ')
            actual_vertex = actual_vertex.predecessor

#The Dijkstra's algorithm does not work with negative cycle