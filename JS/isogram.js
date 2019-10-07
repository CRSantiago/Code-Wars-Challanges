/*
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

isIsogram( "Dermatoglyphics" ) == true
isIsogram( "aba" ) == false
isIsogram( "moOse" ) == false // -- ignore letter case
*/
function isIsogram(str){
  if (typeof str === undefined) {
    return true;
  }
  
  var iso = true;
  
  var str2 = str.toLowerCase();
  
  var counter = {};
  
  for (var i = 0; i < str2.length; i ++) {
    var letter = str2.charAt(i);
    if (counter[letter]) {
      counter[letter] = 1 + counter[letter];
    } else {
      counter[letter] = 1;
    }
    if (counter[letter] > 1) {
      return iso = false;
    }
  }
  return iso;
}
