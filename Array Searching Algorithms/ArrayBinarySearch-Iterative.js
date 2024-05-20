//Binary Search
function binarySearch(arr, n, i, j) {
  while (i <= j) {
    mid = Math.floor(i + (j - i) / 2);
    if (arr[mid] == n) {
      return mid;
    } else if (arr[mid] > n) {
      j = mid - 1;
    } else {
      i = mid + 1;
    }
  }
  return -1;
}
//Array should be sorted
arr = [20, 25, 37, 47, 55, 67, 75, 88, 90];
let i = 0,
  j = arr.length - 1;
const n = 47;
const result = binarySearch(arr, n, i, j);
console.log(result);
