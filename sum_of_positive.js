/*
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20
*/
function positiveSum(arr) {
  let sum = 0;
  for (var p of arr) {
    if(p > 0) {
      sum += p;
    }
  }
  return sum;
}