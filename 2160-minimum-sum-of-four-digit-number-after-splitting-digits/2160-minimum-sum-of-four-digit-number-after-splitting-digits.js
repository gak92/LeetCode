/**
 * @param {number} num
 * @return {number}
 */
var minimumSum = function(num) {
    let s = num.toString().split('').sort();
    // console.log(s);
    
    let new1 = s[0] + s[2];
    let new2 = s[1] + s[3];
    // console.log(new1, new2);
    
    let minSum = parseInt(new1) + parseInt(new2);
    // console.log(minSum);
    
    return minSum;
};