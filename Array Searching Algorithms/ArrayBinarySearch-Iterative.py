##Binary Search Function
def binarySearch(arr,n,i,j):
    while i<=j:
        mid= i+ (j-i)//2
        if arr[mid] == n :
            return mid
        elif arr[mid]<n:
            i=mid+1
        else :
            j=mid-1
    return -1

##Driver Code
arr = [20, 25, 37, 47, 55, 67, 75, 88, 90]
i=0
j=len(arr)-1
n=75
result = binarySearch(arr,n,i,j)
print(result)