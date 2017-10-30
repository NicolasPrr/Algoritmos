import math
import sys
class myGraph (object):
    def __init__(self):

        self.relations = {}
        self.isVisited = {}
        self.distance  = {}
    def __str__(self):
        return str(self.relations)
def add_node(graph, element):
    if element not  in graph.relations:
        graph.relations.update({element:[]})
        graph.isVisited.update({element:[]})
        graph.isVisited[element] = 0
        graph.distance.update({element:[]})
        graph.distance[element] = -10000

# 0 = WHITE, 1 = GRAY, 2 = BLACK
def link_both(graph, element1, element2):
    link(graph, element1, element2)
    link(graph, element2, element1)

def link(graph, origin, destination):
     graph.relations[origin].append(destination)
def restore_graph(graph):
    for element in graph.relations:
        graph.isVisited[element] = 0
        graph.distance[element] = -10000
def BFS(graph, initialElement):
    restore_graph(graph)
    graph.isVisited[initialElement] = 1
    graph.distance[initialElement] = 0
    myQueue = []
    myQueue.append(initialElement)
    while len(myQueue) > 0 :
        node = myQueue.pop(0)
       # print(node)
        dist = graph.distance[node]
        for element in graph.relations[node] :
            if graph.isVisited[element] == 0 :
                graph.isVisited[element] = 1
                graph.distance[element] = dist + 1
                myQueue.append(element)
        graph.isVisited[node] == 2

def DFS(graph, initialElement):
    restore_graph(graph)
    graph.isVisited[initialElement] = 1
    graph.distance[initialElement] = 0
    myQueue = []
    myQueue.append(initialElement)
    while len(myQueue) > 0 :
        node = myQueue.pop()
        dist = graph.distance[node]
        for element in graph.relations[node] :
            if graph.isVisited[element] == 0 :
                graph.isVisited[element] = 1
                graph.distance[element] = dist + 1
                myQueue.append(element)
        graph.isVisited[node] == 2


graph  = myGraph()
T = int(sys.stdin.readline().strip())
for i in range (T - 1):
    A = (sys.stdin.readline().strip().split(" "))
    add_node(graph, A[0])
    add_node(graph, A[1])
    link_both(graph, A[0], A[1])

BFS(graph, '1')
T = int(sys.stdin.readline().strip())
min  = 1000
id = 1000000

for i in range(T):
    b = (sys.stdin.readline().strip())

    if graph.isVisited[b] != 0:

       # print(graph.distance[b] )
      #  print( "mint" + str(min))
        if min >= graph.distance[b] :
            min = graph.distance[b]
        if min >= graph.distance[b] and  id > int(b):
            id = int(b)
print (id)

