import sys 
import random
import timeit
import copy
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
plt.savefig('ex2.jpg')
plt.clf()


# Best case, average case and worst case for bubblesort. Generated with ChatGPT
best_bubble = []
average_bubble = []
worst_bubble = []
for size in sizes:
    # Best case: O(n), already sorted
    a = [i for i in range(size)]
    # Average case: O(n^2), random order
    b = [random.randint(0,10000) for i in range(size)]
    # Worst case: O(n^2), in descending order
    c = [i for i in range(size, 0, -1)]
    # Appending to lists
    best_bubble.append(a)
    average_bubble.append(b)
    worst_bubble.append(c)


# Best case, average case and worst case for quicksort.
# Best case: O(nlogn), random order
best_quick = copy.deepcopy(average_bubble)
# Average case: O(nlogn), random order
average_quick = copy.deepcopy(average_bubble)
# Worst case: O(n^2), in descending order or asecending order (already sorted)
worst_quick = copy.deepcopy(best_bubble)

bestcase_bubble_times = []
averagecase_bubble_times = []
worstcase_bubble_times = []

bestcase_quick_times = []
averagecase_quick_times = []
worstcase_quick_times = []


# Timing and graphing the best cases of each algorithim against eachother
for arr in best_bubble:
    bestcase_bubble_times.append(timeit.timeit(lambda: bubblesort(arr), number = 1 ))

for arr in best_quick:
    bestcase_quick_times.append(timeit.timeit(lambda: quicksort(arr, 0, len(arr) - 1), number = 1 ))

plt.plot(sizes, bestcase_bubble_times, color = 'red', marker = 'o', label = 'Bubble Sort')
plt.plot(sizes, bestcase_quick_times, color = 'blue', marker = 'o', label = 'Quick Sort')
plt.xlabel('Array Size') 
plt.ylabel('Execution Time (seconds)')
plt.title('Best Case Quick Sort vs Best Case Bubble Sort')
plt.legend()
plt.savefig('BC.jpg')
plt.clf()


# Timing and graphing the average cases of each algorithm against eachother
for arr in average_bubble:
    averagecase_bubble_times.append(timeit.timeit(lambda: bubblesort(arr), number = 1))

for arr in average_quick:
    averagecase_quick_times.append(timeit.timeit(lambda: quicksort(arr, 0, len(arr) - 1), number = 1))

plt.plot(sizes, averagecase_bubble_times, color = 'red', marker = 'o', label = 'Bubble Sort')
plt.plot(sizes, averagecase_quick_times, color = 'blue', marker = 'o', label = 'Quick Sort')
plt.xlabel('Array Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Average Case Quick Sort vs Average Case Bubble Sort')
plt.legend()
plt.savefig('AC.jpg')
plt.clf()


# Timing and graphing the worst cases of each algorithim against eachother
for arr in worst_bubble:
    worstcase_bubble_times.append(timeit.timeit(lambda: bubblesort(arr), number = 1))

for arr in worst_quick:
    worstcase_quick_times.append(timeit.timeit(lambda: quicksort(arr, 0, len(arr) - 1), number= 1 ))

plt.plot(sizes, worstcase_bubble_times, color = 'blue', marker = 'o', label = 'Bubble Sort')
plt.plot(sizes, worstcase_quick_times, color = 'red',  marker = 'o', label = 'Quick Sort')
plt.xlabel('Array Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Worst Case Quick Sort vs Worst Case Bubble Sort')
plt.legend()
plt.savefig('WC.jpg')
plt.clf()







