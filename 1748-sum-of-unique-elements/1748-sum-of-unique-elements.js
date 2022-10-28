/**
 * @param {number[]} nums
 * @return {number}
 */
var sumOfUnique = function(nums) {
    let freq = {};
    let total = 0;
    
    for(let num of nums)
    {
        freq[num] = (freq[num] + 1 ) || 1;
    }
    
    for(let key in freq)
    {
        if(freq[key] === 1)
        {
            total += parseInt(key);
        }
    }
    
    return total;
};