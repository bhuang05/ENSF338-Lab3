import timeit
import sys 
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)

# Quick Sort inspired by ChatGPT
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    # Choose the largest element as the pivot
    pivot = arr[-1]  
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)

# Creates a vector of numbers with decreasing values.
def generate_input(size):
    return list(range(size, 0, -1))


def measure_time(input_sizes):
    execution_times = []
    for size in input_sizes:
        setup_code = f'''
from __main__ import quicksort, generate_input
arr = generate_input({size})
'''
        stmt = '''
quicksort(arr)
'''
        execution_time = timeit.timeit(stmt, setup=setup_code, number=1)
        execution_times.append(execution_time)
    return execution_times

# ChatGPT was used to plot the results.
def plot_results(input_sizes, execution_times):
    plt.plot(input_sizes, execution_times, marker='o', linestyle='-')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (s)')
    plt.title('Quicksort Execution Time for Worst-case Inputs')
    plt.grid(True)
    plt.show()

def main():
    # Create vectors of numbers with increasing input sizes. The code didn't plot anything above 5,000 so I limited it to 1,000.
    input_sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    execution_times = measure_time(input_sizes)
    plot_results(input_sizes, execution_times)

if __name__ == "__main__":
    main()