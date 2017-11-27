import math
import sys

def max_heapify(A,i, size) :
    l = i*2 + 1
    r = 2*i + 2
    if l < size  and A[l].weight < A[i].weight :
        largest = l
    else :
        largest = i
    if r < size and A[r].weight  < A[largest].weight :
        largest = r
    if largest != i:
        change  = A[i]
        A[i] = A[largest]
        A[largest] = change
        max_heapify(A, largest, size)

def build_max_heap(A):
    size = len(A)
    for i in range(0, size//2  ):
        j = size//2 - i - 1
        max_heapify(A, j, size)
def heap_sort(A):
    build_max_heap(A)
    for i in range(1, len(A)):
        j = len(A) - i
        change = A[0]
        A[0] = A[j]
        A[j] = change
        max_heapify(A, 0 , j)


#Priority queue

def heap_maximun(A):
    return A[0]
def heap_extract_max(A):
    size = len(A)
    if size < 1:
        print("ERROR ABORT!!")
        return
    max = A[0]
    A[0] = A[size -1]
    A.pop(size-1)
    size = size - 1
    max_heapify(A, 0, size )
    return  max
def heap_increse_key(A,  i , key):
    if key.weight > A[i].weight:
        print ("error")
        return
    A[i] = key
    while i > 0 and A[(i- 1 )//2].weight >   A[i].weight:
        change = A[i]
        A[i ] = A[(i- 1 )//2]
        A[(i- 1 )//2] = change

        i = (i - 1 )//2
def max_heap_insert(A, key):
    size = len(A) + 1
    edge = Edge()
    edge.nodeName = ""
    edge.weight = 1000000
    A.append(edge)
    heap_increse_key(A, size - 1, key)

class myGraph (object):
    def __init__(self):
        self.relations = {}
        self.isVisited = {}
        self.distance  = {}
        self.father = {}
    def __str__(self):
        return str(self.relations)

class Edge (object):
    def __init__(self):
        self.weight  = 0
        self.nodeName = ""
        #self.origin = ""
    def __str__(self):
        return str(self.weight)
    def __str__(self):
        return str(self.nodeName)

    #def __str__(self):
   #     return str(self.origin)


def add_node(graph, element):
    if element  not in graph.relations:
        graph.relations.update({element:[]})
        graph.isVisited.update({element:[]})
        graph.isVisited[element] = 0
        graph.distance.update({element:[]})
        graph.distance[element] = math.inf
        graph.father.update({element: []})
        graph.father[element] = -1

# 0 = WHITE, 1 = GRAY, 2 = BLACK
def link_both(graph, element1, element2, weight1, weight2):
    link(graph, element1, element2,weight1)
    link(graph, element2, element1,weight2)

def link(graph, origin, destination, weight):
     edge = Edge()
     edge.weight = weight
     edge.nodeName = destination
     #edge.origin = origin

     graph.relations[origin].append(edge)

def restore_graph(graph, init):
    for element in graph.relations:
        graph.isVisited[element] = 0
        graph.distance[element] = math.inf
        graph.father[element] = math.inf
    graph.distance[init]  = 0

def relax ( graph , u , v , w):
    if graph.distance[v] >  graph.distance[u]  + w :
        graph.father[v] = u
        graph.distance[v] = graph.distance[u]  + w

def dj (graph, init ):
    #restore_graph(graph, init)
    S = []
    count = 1
    graph.distance[init] = 0
    for element in graph.relations[init]:
        edg = element
        max_heap_insert(S, element)
        relax(graph, init, edg.nodeName, edg.weight)
    sz = len(graph.relations)
    graph.isVisited[init] = 2
   # print(*S)

    while(len(S) > 0   and    count < sz ):
        u = heap_extract_max(S)

      #  print(u.weight)
    #    print("jererada")
    #    print( graph.isVisited[u.nodeName])
        if  graph.isVisited[u.nodeName] == 0 :
            #print("NODO " + str(u.nodeName))
            graph.isVisited[u.nodeName] = 2
            count += 1
            for ele  in graph.relations[u.nodeName]:
                relax(graph , u.nodeName , ele.nodeName , ele.weight)
                max_heap_insert(S,ele)

""""    print
graph = myGraph()
edg = Edge()
add_node(graph , "s" )
add_node(graph , "t" )
add_node(graph , "y" )
add_node(graph , "x" )
add_node(graph , "z" )
link_both(graph,"s", "y" , 5 , 5 )
link_both(graph,"s", "t" , 10 , 5)

link_both(graph,"y", "t" , 3 , 3)
link_both(graph,"y", "x" , 9 , 9)
link_both(graph,"y", "z" , 2 , 2)
link_both(graph,"t", "x" , 1, 1 )
link_both(graph,"t", "y" , 2 , 2 )
link_both(graph,"z", "x" , 6 , 6)

dj(graph,  "s")

print("asdad")
"""

















