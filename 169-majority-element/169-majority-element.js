/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let dict = {};
    let majority = 0;
    let max = 0;
    
    for(let i=0; i<nums.length; i++)
    {
        dict[nums[i]] = (dict[nums[i]] || 0) + 1;
    }
    
    for(const key in dict)
    {
        if(dict[key] > majority) {
            majority = dict[key];
            max = key;
        }
    }
    return max;
};