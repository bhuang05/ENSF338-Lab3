import sys 
import matplotlib.pyplot as plt
import numpy as np
import random

sys.setrecursionlimit(20000)

def bubble_sort(arr):
    comparisons = 0
    swaps = 0

    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            # Increments the comparison count
            comparisons += 1
            if arr[j] > arr[j+1]:
                # Increments the swap count
                swaps +=1
                temp = arr[j]
                arr [j] = arr[j+1]
                arr [j+1] = temp

    return comparisons, swaps

# ChatGPT was used for plotting the data.
def plotting(input_size, comparisons, swaps):
    plt.plot(input_size, comparisons, label='Comparisons', marker='o')
    plt.plot(input_size, swaps, label='Swaps', marker='o')
    plt.xlabel('Input Size')
    plt.ylabel('Count')
    plt.title('Number of Comparisons and Swaps vs Input Size')
    plt.grid(True)
    plt.legend()
    plt.show()

def generate_array(input_size):
    return [random.randint(1,1000) for i in range(input_size)]

def main():
    # Generating arrays of different input sizes to be used in bubble sort.
    input_sizes = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    comparisons_data = []
    swaps_data = []

    for size in input_sizes:
        arr = generate_array(size)
        comparisons, swaps = bubble_sort(arr)
        comparisons_data.append(comparisons)
        swaps_data.append(swaps)

    plotting(input_sizes, comparisons_data, swaps_data)
    

if __name__ == "__main__":
    main()
