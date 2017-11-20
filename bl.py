#'Implementación del grafo sin importa el peso de la arista
import math
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
    def __str__(self):
        return str(self.weight)
    def __str__(self):
        return str(self.nodeName)
def relax ( graph , u , v , w):
    if graph.distance[v] >  graph.distance[u]  + w :
        graph.father[v] = u
        graph.distance[v] = graph.distance[u]  + w


def add_node(graph, element):
    if element not in (graph.relations):
        graph.relations.update({element:[]})
        graph.isVisited.update({element:[]})
        graph.isVisited[element] = 0
        graph.distance.update({element:[]})
        graph.distance[element] = math.inf
        graph.father.update({element: []})
        graph.father[element] = math.inf


# 0 = WHITE, 1 = GRAY, 2 = BLACK
def link_both(graph, element1, element2, weight1, weight2):
    link(graph, element1, element2,weight1)
    link(graph, element2, element1,weight2)

def link(graph, origin, destination, weight):
     edge = Edge()
     edge.weight = weight
     edge.nodeName = destination
     graph.relations[origin].append(edge)

def restore_graph(graph, initElement):
    for element in graph.relations:
        graph.isVisited[element] = 0
        graph.distance[element] = math.inf
    graph.distance[initElement] = 0

def bellman_ford(Graph , s):
    restore_graph(Graph, s)
    for i in range(len(Graph.relations)- 1):
        print("new")
        for element in Graph.relations:
            for vert in Graph.relations[element]:
                relax(Graph, element, vert.nodeName, vert.weight)
                print(" o : " + str(element) + " ->" + str(vert.nodeName) + " " + str(graph.distance[vert.nodeName]))

    for element in Graph.relations:
        for vert in Graph.relations[element]:
            if  Graph.distance[vert.nodeName] > Graph.distance[element] + vert.weight:
                return False
    return  True

def imprimir_recorrido(Graph,F , S):
    t = F
    while Graph.father[t] != math.inf :
        print(str(t) + "->" + str(Graph.father[t]))
        t =  Graph.father[t]
graph = myGraph()
add_node(graph, "S")
add_node(graph, "T")
add_node(graph, "Y")
add_node(graph, "X")
add_node(graph, "Z")

link(graph, "S" ,"Y" , 7)
link(graph, "S" ,"T" , 6)
link(graph, "T" ,"Y" , 8)
link(graph, "T" ,"X" , 5)
link(graph, "T" ,"Z" , -4  )
link(graph, "Y" ,"X" , -3)
link(graph, "Y" ,"Z" ,  9 )
link(graph, "Z" ,"X" ,  7 )
link(graph, "X" ,"T" ,  -2 )
bellman_ford(graph,  "S")

print( graph.distance["Y"] )
imprimir_recorrido(graph , "Z" , "S")
