'''
- Create a matrix for all vertices (2D)
- Set to 0(A-A, B-B, C-C, D-D)/infinity(if we do not have direct path)/concrete nums(when we have current edge)
'''
#TODO: re-watch lecture
INF = 999

def print_solution(nV, distance):
    for i in range(nV):
        for j in range(nV):
            if distance[i][j] == INF:
                print('INF', end=" ")
            else:
                print(distance[i][j], end=" ")
        print(" ")

def floyd_warshall(nV, g): #nV=number of vertices, g=graph
    distance = g
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])

    print_solution(nV, distance)