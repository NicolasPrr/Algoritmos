import math
def cmp(x , y):
    if x == y :
        return 0
    else :
        return math.inf

def cmp_r(x , y):
    if x == y :
        return None
    else :
        return x
class graph_matriz (object):
    def __init__(self):
        self.distance = []
        self.rec  = []

    def initMat(self , N):

        self.distance = [ [ cmp(x, y) for x in range(N)] for y in range(N)]
        self.rec = [[cmp_r(x,y)  for x in range(N)]  for y in range(N)]

    def link(self, fr , to , w):
        self.distance[fr][to] = w
    def link_both(self, fr , to , w):
        self.distance[fr][to] = w
        self.distance[to][fr] = w
    def printM(self):
        for i in range (len(self.rec)):
            print(self.rec[i])
    def printD(self):
        for i in range (len(self.distance)):
            print(self.distance[i])
    def floid_warchal(self):
        fij = 0
        n = len(self.distance)
        for s  in range(n):
            for i in range( n):
                for j in range(n ):
                    if self.distance[i][j] > self.distance[i][s] +self.distance[s][j]:
                        self.distance[i][j] =  self.distance[i][s] +self.distance[s][j]

                        self.rec[i][j] = s




M = graph_matriz()
M.initMat(5)
M.printM()
M.link_both(0, 2, 8)
M.link_both(0, 1, 4)
M.link(1, 2, 1)
M.link_both(1, 3, 2)
M.link_both(2, 3, 4)
M.link_both(2, 4, 2)
M.link_both(3, 4, 7)




M.printD()
M.floid_warchal()
M.printD()
M.printM()

