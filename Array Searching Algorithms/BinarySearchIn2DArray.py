##Search 2D Array
def search2DArray(arr,target):
    #row
    m = len(arr)
    #No Elements in Array
    if(m == 0):
        return False
    #column
    n = len(arr[0])
    left,right = 0,m*n-1
    
    #binary Search
    while(left <= right):
        mid = left + (right-left) //2
        mid_element = arr[mid//n][mid%n]
        if(mid_element == target):
            print("Location : ",mid//n, mid % n)
            return True
        elif(mid_element < target):
            left = mid + 1
        else :
            right = mid - 1
    return False



##Driver Code
arr = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
]
## Sorted 2D Array
## 1. Each Row is Sorted From Right to left
## 2. First Integer of the Each row > Last Integer of Previous Array
target = 3
result = search2DArray(arr,target)
print (result)