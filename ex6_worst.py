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

def searchandsort(arr, key):
    sorted_nums = quicksort(arr, 0, len(arr) - 1)
    index = binarysearch(sorted_nums, 0, len(arr) - 1, key)
    return index

lintimes = []
bintimes = []

listlengths = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
for length in listlengths:
    numbers = [x for x in range(length)] 
    linrez = []
    binrez = []
    for i in range (100):
       
        
        lineartime =  timeit.timeit(lambda: linearsearch(numbers, 1), number=1)
        binarytime =  timeit.timeit(lambda: searchandsort(numbers, 1), number=1)
        
        linrez.append(lineartime)
        binrez.append(binarytime)
    
    linavg = sum(linrez) / len(linrez)
    binavg = sum(binrez) / len(binrez)

    lintimes.append(linavg)
    bintimes.append(binavg)

plt.plot(listlengths, lintimes, label="Linear Search")
plt.plot(listlengths, bintimes, label="Binary Search")
plt.xlabel('List Length')
plt.ylabel('Average Time (s)')
plt.title('Average Speed of Linear and Binary Search')
plt.legend()
plt.show()

#The binary search and quicksort times are exponentially higher than the linear times, to the point where the linear graph is almost a straight line due to the time difference.
#this is no doubt due to the worst case quick sort time for the binary search causing it to take this long.
