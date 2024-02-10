import sys 
import random
import timeit
import copy
import math
import matplotlib.pyplot as plt
sys.setrecursionlimit(20000)


# Bubble sort implementation from slides
def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

# Quicksort implementation from slides
def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)
    return arr

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    done = False;
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


# Creating arrays from size 1-20
sizes = [i**2 for i in range(1, 21)]

# Array intialization
bubble_times = []
quick_times = []
arr1 = []

# Creating random arrays
for size in sizes:
    n = [random.randint(0,10000) for i in range(size)]
    arr1.append(n)

# Deep copying arr1 because bubblesort sorts in place, thus we need to make another array
# Generated with ChatGPT
arr2 = copy.deepcopy(arr1)

# Timing bubblesort
for arr in arr1:
    bubble_times.append(timeit.timeit(lambda: bubblesort(arr), number = 1))

# Timing quicksort
for arr in arr2:
    quick_times.append(timeit.timeit(lambda: quicksort(arr, 0, len(arr) - 1), number = 1))


# Plotting
plt.plot(sizes, bubble_times, color='red', label='Bubble Sort')
plt.plot(sizes, quick_times, color='blue', label='Quick Sort')
plt.xlabel('Array Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Bubble Sort vs Quick Sort')
plt.legend()
plt.savefig('ex1.jpg')
plt.clf()

# Best case, average case and worst case for bubblesort. Generated with ChatGPT
# Best case: O(n), already sorted
best_bubble = [i for i in range(1, 2500)]
# Average case: O(n^2), random order
average_bubble = [random.randint(0,10000) for i in range(1,2500)]
# Worst case: O(n^2), in descending order
worst_bubble = [i for i in range(2500, 1, -1)]

# Best case, average case and worst case for quicksort. Generated with ChatGPT
# Best case: O(nlogn), already sorted
best_quick = copy.deepcopy(best_bubble)
# Average case: O(nlogn), random order
average_quick = copy.deepcopy(average_bubble)
# Worst case: O(n^2), in descending order
worst_quick = copy.deepcopy(worst_bubble)

# Timing bubblesort cases
time_best_bubble = timeit.timeit(lambda: bubblesort(best_bubble), number=1)
time_average_bubble = timeit.timeit(lambda: bubblesort(average_bubble), number=1)
time_worst_bubble = timeit.timeit(lambda: bubblesort(worst_bubble), number=1)

# Timing quicksort cases
time_best_quick = timeit.timeit(lambda: quicksort(best_quick, 0, len(best_quick) - 1), number=1)
time_average_quick = timeit.timeit(lambda: quicksort(average_quick, 0, len(average_quick) -1), number=1)
time_worst_quick = timeit.timeit(lambda: quicksort(worst_quick, 0, len(worst_quick) - 1), number=1)

# Plot the results, generated with ChatGPT
plt.plot(['Best Case', 'Average Case', 'Worst Case'], [time_best_bubble, time_average_bubble, time_worst_bubble], label='Bubble Sort')
plt.plot(['Best Case', 'Average Case', 'Worst Case'], [time_best_quick, time_average_quick, time_worst_quick], label='Quick Sort')
plt.xlabel('Case')
plt.ylabel('Time (s)')
plt.title('Comparison of Bubble Sort and Quick Sort')
plt.legend()
plt.savefig('ex1_cases.jpg')





