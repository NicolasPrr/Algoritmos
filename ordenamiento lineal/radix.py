import math
def sizeStr(x):
    #retorna el tamaño del numero
    return len(str(x))
def initQ(mtr):
    for i in range(10):
        mtr.append([])
def maxSizeLen(A):
    max = -math.inf
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
        #print("#asda")
        #print(dr[i])
        for j in range(len( dr[i])):
            s = dr[i].pop(0)
            Bs.append(s)

    return Bs

def Mradix(As):
    maxSize = maxSizeLen(As)
    dr = []
    for i in range(maxSize):
        dr = []
        initQ(dr)
        for j in range(len(As)):
            number= (str(As[j]))
            if len(number) - 1 < i  :
                dr[0].append(As[j])
            else:
                #print(A[j])
                n = len(str(number)) - i - 1
                dr[int(number[n])].append(As[j])

        As = rmp_array(As, dr)
    return As
        
B =[10, 15 , 1, 60, 5, 100,  25, 50   ]
B = Mradix(B)
print (B)
