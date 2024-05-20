//findSum
function findSum(arr, i, j, n) {
  while (i <= j) {
    if (arr[i] + arr[j] == n) {
      return [i, j];
    } else if (arr[i] + arr[j] < n) {
      i = i + 1;
    } else {
      j = j - 1;
    }
  }
  return -1;
}

let arr = [20, 40, 60, 80, 90, 120, 240];
let i = 0;
let j = arr.length - 1;
let n = 210;
let result = findSum(arr, i, j, n);
console.log(result);
