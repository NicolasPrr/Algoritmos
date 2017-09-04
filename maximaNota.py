import sys


T = int(sys.stdin.readline().strip())


i = 0
j = 0



for j in range(0,T):
    print ("Caso #" + str( j + 1 ) + ":")
    N = int(sys.stdin.readline().strip())
    names = []
    max = -1000000
    for  i in range(0, N):
        S = (sys.stdin.readline().strip().split(' '))
        myNum = (int(S[1]))
        if myNum > max :
            names = []
            max = myNum
            names.append(S[0])
           
            
        elif myNum == max: 
            
            names.append(S[0])
            #print(names)
    names.sort()
    for i in range(0, len(names)):
        print(names[len(names)-1-i])
            
    print("")
