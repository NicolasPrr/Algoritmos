import math
#with decimals
def sortInsertion(Array):
    j = 1
    for j  in range(1, len(Array)):
        key = Array[j]
        i = j -1
        while i > -1 and Array[i] > key:
            Array[i  + 1 ] = Array[i]
            i = i - 1
        Array[i + 1 ] = key
def setValues (B):
    S = []
    for i in range(len(B)):
        for j in range(len (B[i])):
            S .append(B[i][j])
    return S
def initQ(mtr , n):
    for i in range(n):
        mtr.append([])
def bucket_sort(A):
    n = len(A)
    B = []
    initQ(B, n)
    for i in range(n):
        s = int( n*A[i])
        B[s].append(A[i])
    for i in range(n):
        sortInsertion(B[i])

    print (setValues(B))

A = [0.78 , 0.17 , 0.39, 0.26 , 0.72, 0.94 , 0.21 , 0.12, 0.23, 0.68]
bucket_sort(A)
