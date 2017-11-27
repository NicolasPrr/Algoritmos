import sys


def min_costo(V):
    N = len(V)
    C = [[0 for j in range(N)] for i in range(N)]
    for i in range(N - 1, -1, -1):
        for j in range(N -1, i, -1):
            min = float('Inf')
            for k in range(j, i, -1):
                value = V[i][k] + C[k][j]
                if value < min:
                    min = value
            C[i][j] = min
    return C


T = int(sys.stdin.readline().strip())
for i in range(T):
    N = int(sys.stdin.readline().strip())
    C = []
    for j in range(N):
        D = list(map(int, sys.stdin.readline().strip().split(" ")))
        C.append(D)
    F  = min_costo(C)
    for j in range(N):
        print(*F[j])
