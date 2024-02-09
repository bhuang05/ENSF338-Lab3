import sys 
import matplotlib.pyplot as plt
import numpy as np

sys.setrecursionlimit(20000)

def bubble_sort(arr):
    arr_size = len(arr)
    comparisons = 0
    swaps = 0

    n = len(arr)
    for i in range(n):
        # Increments the comparison count
        comparisons += 1
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Increments the swap count
                swaps +=1
                temp = arr[j]
                arr [j] = arr[j+1]
                arr [j+1] = temp

    
    arr, comparisons, swaps = bubble_sort(arr)
    plotting(arr_size, comparisons, swaps)

# ChatGPT was used for the plotting function.
def plotting(input_size, comparisons, swaps):
    input_size = np.array(input_size)
    
    # Plotting comparisons
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(input_size, comparisons, label='Comparisons', marker='o')
    plt.title('Number of Comparisons vs Input Size')
    plt.xlabel('Input Size')
    plt.ylabel('Number of Comparisons')
    plt.grid(True)
    plt.legend()

    # Plotting swaps
    plt.subplot(1, 2, 2)
    plt.plot(input_size, swaps, label='Swaps', marker='o')
    plt.title('Number of Swaps vs Input Size')
    plt.xlabel('Input Size')
    plt.ylabel('Number of Swaps')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

def generate_array(input_size):
def main():
    # Manually entering elements inside the array

    # Array 1 with input size 4 
    arr1 = [64, 34, 25, 12]
    bubble_sort(1)

    # Array 2 with input size 8
    arr2 = [91, 12, 33, 45, 67, 89, 23, 56]

    # Array 3 with input size 16

    # Array 4 with input size 32

    # The rest of the code is unfinished.
    

if __name__ == "__main__":
    main()