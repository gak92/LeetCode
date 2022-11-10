/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfFour = function(n) {
    // n=16 ===>   16/4 ===> 4/4  ===> 1
    // n=5 ===> 5/4   ===> 1.21, 5//4 ==> 1 ===> 4 ===> 0
    
    if(n===0)
        return false;
    
    if(n===1)
        return true;
    
    while(n % 4 === 0)          // 16 % 4 ===> 4, 4%4 ===> 0, 5 % 4 ==> 1, 1..2%4 ==> 0
    {
        n = n / 4;              // 16/4 ===> 4 ,    4/4 = 1, 5/4 ==>1.222
    }
    
    return n===1 ? true : false;
    
};