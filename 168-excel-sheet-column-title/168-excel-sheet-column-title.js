/**
 * @param {number} columnNumber
 * @return {string}
 */
var convertToTitle = function(columnNumber) {
  let res = "";

  while(columnNumber > 0)
  {
      let remainder = columnNumber % 26;
      columnNumber = parseInt(columnNumber / 26);
      // console.log(columnNumber);
      if(remainder == 0) {
          res = "Z" + res;
          columnNumber -= 1;
      }
      else {
          res = String.fromCharCode(64+remainder) + res;
      }
  }
    
  return res;
};
