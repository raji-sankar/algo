import sys

from collections import namedtuple
Edge = namedtuple('Edge', 'start end weight')









class Graph(object):
    def __init__(self, n, edges):
        self.n = n
        self.vertices = range(n)
        self.edges = [Edge(edge[0], edge[1], edge[2]) for edge in edges] + \
                        [Edge(edge[1], edge[0], edge[2]) for edge in edges]

    def get_edges(self, v):
        return [edge for edge in self.edges if edge.start == v]







def dijkstra(g, s):
    intree = [False] * g.n
    distance = [-1] * g.n
    parent = [-1] * g.n

    distance[s] = 0
    v = s
    while not intree[v]:
        intree[v] = True
        for edge in g.get_edges(v):
            w = edge.end
            weight = edge.weight
            if distance[w] > distance[v] + weight:
                distance[w] = distance[v] + weight
                parent[w] = v

        v = 1
        dist = 10000 # a big number
        for i in g.vertices:
            if not intree[i] and dist > distance[i]:
                dist = distance[i]
                v = i


    return distance



t = int(raw_input().strip())
for i in range(t):
    n, m = map(int, raw_input().strip().split())
    edges = []
    for j in range(m):
        x, y, r = map(int, raw_input().strip().split())
        edges.append((x-1, y-1, r))
    s = int(raw_input().strip())
    g = Graph(n, edges)
    print n
    for edge in g.edges:
        print '{0} {1} {2}'.format(edge.start + 1, edge.end + 1 , edge.weight)

    # print dijkstra(g, s-1)
