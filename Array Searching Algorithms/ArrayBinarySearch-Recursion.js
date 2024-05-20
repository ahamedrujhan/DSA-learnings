//Binary Search
function binarySearch(arr, n, i, j) {
  while (i <= j) {
    mid = Math.floor(i + (j - i) / 2);
    if (arr[mid] == n) {
      return mid;
    } else if (arr[mid] < n) {
      return binarySearch(arr, n, mid + 1, j);
    } else {
      return binarySearch(arr, n, i, mid - 1);
    }
  }
  return -1
}
//Driver Code
let n = 55;
//Array should be sorted
let arr = [20, 25, 37, 47, 55, 67, 75, 88, 90];
let i = 0;
let j = arr.length - 1;
let result = binarySearch(arr, n, i, j);
console.log(result);

/*
Psudo Code
i=0,j=arr.length-1,n=55
binarySearch(arr,n,i,j){
   while(i<=j) {
    mid = i+ (j-i)/2
if(arr[mid]==n){
    return mid
}
else if(arr[mid]<n){
    return binarySearch(arr,n,mid+1,j)
}
else {
    return binarySearch(arr,n,i,mid-1)
}
}
return -1
}
*/