import math

def initQ(mtr):
    for i in range(10):
        mtr.append([])
def maxSizeLen(A):
    max = -100000000
    for i in range(0, len(A)):
        if max < A[i]:
            max = A[i]
    return len(str(max))
def printM(A):
    for i in range(len(A)):
        print( str(i) + ": " +  str(A[i]))
def rmp_array(Bs, dr):
    Bs = []
    for i in range(len(dr)):
        for j in range(len( dr[i])):
            s = dr[i].pop(0)
            Bs.append(s)

    return Bs

def Mradix(As):
    maxSize = maxSizeLen(As)
    dr = []
    mydiv = 1
        
    for i in range(maxSize):
        dr = []
        initQ(dr)
        
        print(mydiv)
        for j in range(len(As)):
            if As[j] // mydiv == 0:
              dr[0].append(As[j])
            else:
              dr[(As[j] //(mydiv)) % 10].append(As[j])
        mydiv*=10
        printM(dr)
        
        As = rmp_array(As, dr)
    return As
        
B =[10, 15 , 1, 60, 5, 100,  25, 50   ]
B = Mradix(B)

print (B)
