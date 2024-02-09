import sys 
import timeit
import matplotlib.pyplot as plt
import numpy as np
import random 

sys.setrecursionlimit(20000)

def quicksort(arr, low, high):
    if low < high:
        piv = partition(arr, low, high)
        quicksort(arr, low, piv - 1) 
        quicksort(arr, piv + 1, high)
    return arr  

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right


def linearsearch(data, key):
    for index, value in enumerate(data):
        if key == value:
            return index
    return -1

def binarysearch(data, first, last, key):
    if(first <= last):
        mid = (first+last) // 2
    if(key == data[mid]):
        return mid
    elif (key < data[mid]):
        return binarysearch(data, first, mid-1, key)
    elif (key > data[mid]):
        return binarysearch(data, mid+1, last, key)
    return -1

lintimes = []
bintimes = []

listlengths = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
for length in listlengths:
    numbers = [x for x in range(length)] 
    linrez = []
    binrez = []
    for i in range (100):
        random.shuffle(numbers)
        sortednums = quicksort(numbers, 0 , len(numbers)-1)
        
        
        lineartime =  timeit.timeit(lambda: linearsearch(numbers, 1), number=100)

        binarytime =  timeit.timeit(lambda: binarysearch(sortednums, 0, len(sortednums)-1, 1), number=100)
        
        linrez.append(lineartime/100)
        binrez.append(binarytime/100)
    
    linavg = sum(linrez) / len(linrez)
    binavg = sum(binrez) / len(linrez)

    lintimes.append(linavg)
    bintimes.append(binavg)

plt.plot(listlengths, lintimes, label="Linear Search")
plt.plot(listlengths, bintimes, label="Binary Search")
plt.xlabel('List Length')
plt.ylabel('Average Time (s)')
plt.title('Average Speed of Linear and Binary Search')
plt.legend()
plt.show()



