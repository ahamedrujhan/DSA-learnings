#function definition
#timecomplexity O(n)
def findMaxProfit(price):
    minPrice = float('inf')
    maxProfit=0
    for i in range(len(price)):
        if (price[i]<minPrice):
            minPrice = price[i]
        elif price[i] - minPrice > maxProfit :
            maxProfit = price[i] - minPrice
    return maxProfit




#Driver Code
Price=[7,1,5,3,6,4]
maxProfit=findMaxProfit(Price)
print(maxProfit)