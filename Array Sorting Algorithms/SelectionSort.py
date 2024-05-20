# Time Complexity is O(n^2)
# Selection Sort Function
def selectionSort(arr):
    i = 1  # pointer to start selecting elements
    while i < len(arr):  # loop to run until end of the array
        j = i - 1  # Start to compare with previous elements
        key = arr[i]  # Set the comparing value

        while (
            j >= 0 and key < arr[j]
        ):  # loop to check if the previous elements are biger or not
            arr[j + 1] = arr[j]  # if it is Swap it to next to it
            j = j - 1  # set the pointer to previous element until start of the array
        arr[j + 1] = (
            key  # if not the previous elements are bigger then key element then add it
        )
        i = i + 1  # Set the pointer to next element
    return arr  # finally return sorted array


# Driver Code
arr = [70, 20, 50, 30, 90, 5, 15]
results = selectionSort(arr)
print(results)
