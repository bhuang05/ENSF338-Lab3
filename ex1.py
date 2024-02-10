def merge_sort(arr, low, high):
    if low < high: 
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1,high)
        merge(arr, low, mid, high)

#Merge function design based off example from ChatGPT
def merge(arr,low,mid,high):
    len1 = mid - low + 1
    len2 = high - mid

    temp1 =   [0] * len1
    temp2 = [0] * len2

    for i in range (0, len1):
        temp1[i] = arr[low+i]

    for i in range (0, len2):
        temp2[i] = arr[mid + 1 + i]

    i = 0     
    j = 0     
    k = low 

    while i < len1 and j < len2:
        if temp1[i] <= temp2[j]:
            arr[k] = temp1[i]
            i += 1
        else:
            arr[k] = temp2[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = temp1[i]
        i += 1
        k += 1

    while j < len2:
        arr[k] = temp2[j]
        j += 1
        k += 1   

