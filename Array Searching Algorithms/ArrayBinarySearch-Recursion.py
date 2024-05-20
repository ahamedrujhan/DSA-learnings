#Binary Search
def binarySearch(arr,n,i,j):
    while i<=j:
        mid = i + (j-i)//2
        if arr[mid] == n:
            return mid
        elif arr[mid]<n:
            ##reducing the array left searching area
            ##Recusion in th method definition
            return binarySearch(arr,n,mid+1,j)
        else:
             ##reducing the array right searching area
            ##Recusion in th method definition
            return binarySearch(arr,n,i,mid-1)
    return -1

#Driver Code
# Array Should be Sorted
arr = [20, 25, 37, 47, 55, 67, 75, 88, 90]
i=0
j=len(arr)-1
n=90
result = binarySearch(arr,n,i,j)
print(result)