/**
 * @param {number[]} nums
 * @return {number[]}
 */
var numberOfPairs = function(nums) {
    let freq = {};
    let pairs = 0, leftover = 0;
    
    for(let num of nums)
    {
        if(freq[num] > 0)
            freq[num] += 1
        else
            freq[num] = 1
    }
    
    for(const key in freq)
    {
        pairs += parseInt(freq[key] / 2);
        leftover += freq[key]%2;
    }
    
    console.log([pairs, leftover]);
    return [pairs, leftover];
};

    