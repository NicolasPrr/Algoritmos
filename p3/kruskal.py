
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
class Edge (object):
    def __init__(self):
        self.weight  = 0
        self.origin = ""
        self.dest= ""

        #self.origin = ""
    def __str__(self):
        return str(self.weight)
    def __str__(self):
        return str(self.origin)
def find_set(A, u):
    x = u
    while(A[x] != x):
        x = A[x]
    return x

def kruskal():
    S = []
    n = 10
    #leemos el  numero de vertices
    d = [i for i in range (n)]
    edge = Edge()
    edge.origin = 1
    edge.dest = 2
    edge.weight = 6
    max_heap_insert(S ,edge)
    edge.origin = 1
    edge.dest = 3
    edge.weight = 2
    max_heap_insert(S, edge)
    edge.origin = 7
    edge.dest = 8
    edge.weight = 10
    max_heap_insert(S, edge)
    n = len(S)


kruskal()
