#function finding the sum
def findSum(arr,i,j,n) :
    while(i<=j):

        if  (arr[i]+arr[j]==n):
            return i,j
        elif    (arr[i]+arr[j]<n):
            i=i+1
        else :
            j=j-1
    return -1


##Driver 
arr=[20,40,60,80,90,120,240]
# Array Should Be Sorted
i=0
j=len(arr)-1
n=210
result=findSum(arr,i,j,n)
print(result)