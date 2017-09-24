import random, time, gc, math, sys

def shuffle(list):
    for j in range(0,len(list)-1):
        r1 = random.randint(0, len(list)-1)
        list[j],list[r1] = list[r1],list[j]
    return list

def createList(n):

    list = []

    for i in range(0,n):
        list.append(i + 1)
    return list

def mergeSort(arr,p,r):
    if p < r:
        q = (p + r) // 2
        mergeSort(arr, p, q)
        mergeSort(arr, q + 1, r)
        merge(arr, p, q, r)

def merge(arr, low, med, max):
    l = med - low + 1
    r = max - med

    left= arr[low:med + 1]
    right = arr[med + 1:max + 1]

    left.append(sys.maxsize)
    right.append(sys.maxsize)

    i = 0
    j = 0

    for k in range(low,max):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1

size = int(input())

for k  in range(0, 9):

    array = createList(size)
    shuffle(array)

    start_time = time.time()
    mergeSort(array, 0, len(array) - 1)
    print(str((time.time() - start_time)*1000))
    gc.collect()
