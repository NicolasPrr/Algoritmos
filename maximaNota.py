#Dado unos estudiantes con notas, se tiene que imprimir los que tengan la mayor nota

import sys
def swap (list, i , j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp


def insertionSort(alist, names):
   for index in range(1,len(alist)):
     currentvalue = alist[index]
     position = index
     nowIndex = names[index]
     while position>0 and alist[position-1]>currentvalue:

         alist[position]=alist[position-1]
         names[position] =  names[position-1]
         position = position-1

     alist[position]= currentvalue
     names[position] = nowIndex


T = int(sys.stdin.readline().strip())


i = 0
j = 0



for j in range(0,T):
    print ("Caso #" + str( j + 1 ) + ":")
    N = int(sys.stdin.readline().strip())
    names = []
    notes = []
    for  i in range(0, N):
        S = (sys.stdin.readline().strip().split(' '))
        names.append(S[0])
        notes.append(int(S[1]))
    insertionSort(notes, names)
    i = 1
    mayor = notes[N-i]
    isEqual = True
    while (isEqual):

        print (names[N - i])
        i = i + 1
        if (notes[N-i] != mayor and i > 1):
            isEqual = False



    print("")
