import sys 
import random
import timeit
import copy
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize
sys.setrecursionlimit(20000)

# Insertion sort implementation from slides
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Binary insertion sort implementation from https://www.geeksforgeeks.org/binary-insertion-sort/
def binary_search(arr, val, start, end):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start+1
 
    if start > end:
        return start
 
    mid = (start+end)//2
    if arr[mid] < val:
        return binary_search(arr, val, mid+1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid-1)
    else:
        return mid
 
 
def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i-1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
    return arr


# Creating arrays from size 1-20 
sizes = [i**3 for i in range(1, 21)]

# Array intialization
insertion_times = []
binary_insertion_times = []
arr1 = []

# Creating random arrays for the average cases of insertion sort and binary insertion sort
for size in sizes:
    n = [random.randint(0,10000) for i in range(size)]
    arr1.append(n)

# Deep copy of arr1
arr2 = copy.deepcopy(arr1)

for arr in arr1:
    insertion_times.append(timeit.timeit(lambda: insertion_sort(arr), number = 1))

for arr in arr2:
    binary_insertion_times.append(timeit.timeit(lambda: binary_insertion_sort(arr), number = 1))

# Plotting without fitting, as the data is accurate thanks to the size of input data
plt.plot(sizes, insertion_times, color='red', label='Insertion Sort')
plt.plot(sizes, binary_insertion_times, color='blue', label='Binary Insertion Sort')
plt.xlabel('Array Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Insertion Sort vs Binary Insertion Sort (No interpolation)')
plt.legend()
plt.show()
plt.clf()

# Note that the average case for insertion sort and binary insertion sort are both O(n^2), thus a quadratic fit is appropriate
# Lines 84-107 generated with ChatGPT

# Define the function to fit (n^2)
def quadratic_func(n, a, b):
    return a * n**2 + b

# Fit the curve to the data
popt_insertion, pcov_insertion = scipy.optimize.curve_fit(quadratic_func, sizes, insertion_times)
popt_binary, pcov_binary = scipy.optimize.curve_fit(quadratic_func, sizes, binary_insertion_times)


# Plot the data points
plt.scatter(sizes, insertion_times, label='Insertion Sort')
plt.scatter(sizes, binary_insertion_times, label='Binary Insertion Sort')
# Plot the quadratic curve
fitted_values_insertion = quadratic_func(np.array(sizes), *popt_insertion)
plt.plot(sizes, fitted_values_insertion, 'r', label='Quadratic Fit (Insertion Sort)')
fitted_values = quadratic_func(np.array(sizes), *popt_binary)
plt.plot(sizes, fitted_values, 'b', label='Quadratic Fit')


plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Quadratic Interpolation for Binary Insertion Sort')
plt.legend()
plt.show()



"""
Question 4:
Just from looking at the graphs, we can see that binary insertion sort is faster than insertion sort. 
Although they both have the same average case time complexity, binary insertion sort makes less comparisons 
than insertion sort thanks to the calculation of the "mid" variable.
"""