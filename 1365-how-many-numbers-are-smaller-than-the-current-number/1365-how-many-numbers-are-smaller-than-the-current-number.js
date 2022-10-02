/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {
    let smaller = [];
    
    for(let i=0; i<nums.length; i++)
    {
        smaller[i] = 0;
    }
    
    for(let i=0; i<nums.length; i++)
    {
        for(let j=0; j<nums.length; j++)
        {
            if(i !== j && nums[i]> nums[j])
            {
                smaller[i] += 1;
            }
        }
    }
    
    return smaller;
};