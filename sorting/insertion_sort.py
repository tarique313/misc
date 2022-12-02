def insertionSort(arr):
    for i in range(1, len(arr)): # Travers through 1 to array length
        j = i - 1
        while j >= 0 and arr[j+1] < arr[j]:
            temp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = temp
            j-=1
    return arr

print(insertionSort([4,3,2,1]))
