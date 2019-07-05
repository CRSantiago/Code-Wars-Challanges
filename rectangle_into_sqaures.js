/*
The drawing below gives an idea of how to cut a given "true" rectangle into squares ("true" rectangle meaning that the two dimensions are different).


Can you translate this drawing into an algorithm?

You will be given two dimensions

a positive integer length (parameter named lng)
a positive integer width (parameter named wdth)
*/
function sqInRect(lng, wdth){
  if (lng === wdth) return null;
  let sqrArr = [];
  while (lng * wdth > 0) {
    if (lng > wdth) {
      sqrArr.push(wdth);
      lng = lng - wdth;
    } else {
      sqrArr.push(lng);
      wdth = wdth - lng;
    }
  }
  return sqrArr;
}