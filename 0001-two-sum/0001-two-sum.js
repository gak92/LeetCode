/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    
    let complement = {};
    
    for(let i=0; i<nums.length; i++)
    {
        complement[nums[i]] = i;
    }    
    console.log(complement);
    for(let i=0; i<nums.length; i++)
    {
        let x = target - nums[i];
        if(x in complement && i!== complement[x])
        {
            return [i, complement[x]]
        }
    }
    
    
    // for(let i=0; i<nums.length-1; i++)
    // {
    //     let x = nums[i];
    //     for(let j=i+1; j<nums.length; j++)
    //     {
    //         if(nums[j] === target-x)
    //         {
    //             return [i,j];
    //         }
    //     }
    // }
    
    
//     Brute force approach
    // for(let i=0; i<nums.length-1; i++)
    // {
    //     for(let j=i+1; j<nums.length; j++)
    //     {
    //         if((nums[i]+nums[j]) === target)
    //         {
    //             return [i, j];
    //         }
    //     }
    // }
};