/**
 * @param {number[]} nums
 * @return {number[]}
 */
var buildArray = function(nums) {
//     let ans = [];
//     for (let i=0; i<nums.length; i++) {
//         ans[i] = nums[nums[i]];
//     }
    
//     return ans;
    let len = nums.length;
    
    for (let i=0; i<len; i++) {
        nums[i] = len * (nums[nums[i]] % len) + nums[i];
    }
    
    for (let i=0; i<len; i++) {
        nums[i] = Math.floor(nums[i] / len);
    }
    
    return nums;    
    
};
