/**
 * @param {number[]} nums
 * @return {number}
 */

let swap = (nums, i, j) => {
    let temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
}
var maxProduct = function(nums) {
    
    for(let i=0; i<nums.length-1; i++)
    {
        for(let j=i; j<nums.length; j++)
        {
            if(nums[i] > nums[j])               
            {
                swap(nums, i, j);
            }
        }
    }
    
    
    
    console.log(nums);
    
    return ((nums[nums.length-1]-1) * (nums[nums.length-2] -1))
    
    
    // nums.sort((a,b)=>b-a);
    // return ((nums[0]-1) * (nums[1]-1));
};