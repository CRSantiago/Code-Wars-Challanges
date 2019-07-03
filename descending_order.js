/*
Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 21445 Output: 54421

Input: 145263 Output: 654321

Input: 1254859723 Output: 9875543221
*/

//The very difficult way I did it the first time. 
function descendingOrder(n){
  var arr = n.toString().split('').map(Number);
  var sortedArr = arr.sort((a,b) => b - a);
  var result = sortedArr.join('');
  var final = parseInt(result);
  return final;
}

//Much cleaner second attempt
function descendingOrder(n) {
  return parseInt(n.toString().split("").sort().reverse().join(""));
}