function countPositivesSumNegatives(input) {

if(input === null || input.length < 1) {
  return [];
}

var newArr = [0,0];
var count;
input.forEach((cur) => {
  if(cur > 0) {
    newArr[0] += 1;
  } else {
    newArr[1] += cur;
  }
});

return newArr;
}