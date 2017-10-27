import math
def COUNTIGN_SORT(A , B ):
    C =[]
    max = -math.inf
    min = math.inf
    for i in range(len(A)):
        if max < A[i]:
            max = A[i]
        if min > A[i]:
            min = A[i]
        B.append(math.inf)
    k = max - min + 1
    for i in range(0 , k ):
        C.append(0)
    for j in range(0, len(A)):
        C[A[j]- min] =  C[A[j]- min ]  + 1
    for i  in range (1, k  ):
        C[i] = C[i] + C[ i - 1  ]
    for j  in range( 0 , len(A)):
        B[C[A[j] - min]  -1] = A[j]  #10 -> 1
        C[A[j] - min ] = C[A[j]- min]  - 1
#A = [10 , 3 ,3,8 , 1 , 5 ,7 ,0 , 1 ,3 , 5, 20 ]
A =  [9 , 4 , 10 , 8 , 2, 4 ]
B = []

# K = MAX - MIN + 1
COUNTIGN_SORT(A, B)
print(B)
