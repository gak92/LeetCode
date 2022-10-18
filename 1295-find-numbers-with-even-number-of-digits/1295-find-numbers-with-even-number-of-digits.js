/**
 * @param {number[]} nums
 * @return {number}
 */
var findNumbers = function(nums) {
    let count = 0;
    
    for(let num of nums)
    {
        let digit = 0;
        while(num !== 0)
        {
            num = Math.floor(num / 10);
            digit += 1;
        }
        if(digit % 2 === 0)
        {
            count +=1;
        }
    }
    
    console.log(count);
    return count;
};