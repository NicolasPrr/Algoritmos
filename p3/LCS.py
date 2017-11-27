def  lcs_length(X , Y):
    m = len(X) + 1
    n = len(Y) + 1
    C = [[ 0 for  y in range(n)] for x in range(m)] # M FILAS, N COLUMNAS
    D = [[0 for y in range(n)] for x in range(m)]  # M FILAS, N COLUMNAS
    #LLENAMOS LAS DOS MATRICES CON 0

    for i in range(1,m):
       for j in range(1,n):
           if X[i-1] == Y[j-1]:
               C[i][j] = C[i-1][ j - 1 ] + 1
               D[i][j] = "LU"
           elif C[i -1][j] >= C[i][j -1]:
               C[i][j] = C[i-1][j]
               D[i][j]  = "U"
           else:
               C[i][j] = C[i][ j - 1]
               D[i][j] = "L"
    return C, D

def printLSC(b, X , i , j ,ST):
    t = ST
    if  i == 0 or j == 0:
        print(t)
        return
    if b[i][j] == "LU":
        t = (X[i - 1])  + t
      #  print(t)
        printLSC(b,X, i - 1 , j - 1 ,t)
        #PRINT(x[x-1])
    elif  b[i][j] == "U":
        printLSC(b,X, i -1 , j, t)
    else :
        printLSC(b,X, i, j - 1, t)

def printD(X):
    for i in range(len(X)):
         print(X[i])

x = "ABCBDAB"
y = "BDCABA"
A , B = lcs_length(x , y)
printD(B)

print(printLSC(B,x  ,len(x) , len(y) , ""))

