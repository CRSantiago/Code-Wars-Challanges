// Given an array, find the int that appears an odd number of times.

// There will always be only one integer that appears an odd number of times.

function findOdd(A) {
  var count = 0;
  
  for(var i = 0; i < A.length; i++){
    for(var j = 0; j < A.length; j++) {
        if(A[i] == A[j]) {
          count++;
        }
      }
      if(count % 2 == 1) {
        return A[i];
      }
  }
  return count;
}