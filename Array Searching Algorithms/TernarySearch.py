#Ternary Search
def ternarySearch(arr,target,i,j):
  
    while (i<=j):
        mid1 = i + (j-i) // 3
        mid2 = j - (j-i) //3
        if (arr[mid1] == target ):
            return mid1
        elif(arr[mid2] == target):
            return mid2
        #first part of ternary search
        elif(arr[mid1]> target):
            return ternarySearch(arr,target,i,mid1-1)
            #third part of ternary search
        elif(arr[mid2]<target):
           return  ternarySearch(arr,target,mid2+1,j)
            #second part of ternary search
        else:
            return ternarySearch(arr,target,mid1+1,mid2-1)
        #Searching elememt is not found
    return -1



##Driver Code
arr= [20,45,27,47,55,67,75,88,90]
target = 27
i = 0
j = len(arr) -1
result = ternarySearch(arr,target,i,j)
print(result)