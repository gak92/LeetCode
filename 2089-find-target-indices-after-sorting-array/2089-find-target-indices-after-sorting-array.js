/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var targetIndices = function(nums, target) {
    let sortedNums = nums.sort((a,b) => a-b);
    let res = [];
    
    for (let i=0; i<sortedNums.length; i++)
    {
        if(target === sortedNums[i])
        {
            res.push(i);
        }
    }
    
    return res;
};