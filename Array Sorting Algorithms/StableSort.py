# Time Complexity O(n*n)
# Stable Sort
def stableSort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if arr[min] > arr[j]:
                # finding minimum index
                min = j
        # Swapping the element
        arr[i], arr[min] = arr[min], arr[i]
    return arr


##Driver Code
arr = [70, 20, 50, 60, 35, 47]
result = stableSort(arr)
print(result)
