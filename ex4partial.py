import sys 
sys.setrecursionlimit(20000)

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    done = False

    while not done:
        # Keep traversing until the left pointer sees an element > pivot and right pointer sees an element < pivot
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while right >= left and arr[right] >= pivot:
            right = right - 1
        if right < left:
            done = True
        else:
            # Switch the left and right values of the array
            arr[left], arr[right] = arr[right], arr[left]
    
    arr[low], arr[right] = arr[right], arr[low]
    return right

    

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, high)
        quicksort(arr, pivot_index+1, high)

def main():
    # Create an array that is the worst case scenario 
    print("The function is still not finished")

    # The rest of the code is unfinished

if __name__ == "__main__":
    main()
    