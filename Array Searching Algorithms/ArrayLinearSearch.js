let arr = [20, 45, 27, 47, 55, 67, 75, 88, 90];
function find(arr, n) {
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] == n) {
      return i;
      break;
    }
  }
  return -1;
}
console.log(find(arr, 67));

/* 
Psudo code
 arr =[array contents]
x = arr.length
for i in range(0,x){
    if(arr[i] == n ) {
        return i;
        break;
    }
}
return -1;
*/
