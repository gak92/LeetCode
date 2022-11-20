/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minimumDifference = function(nums, k) {
    nums.sort((a,b) => a - b);
    let left = 0;
    let right = k - 1;
    let minDiff = Infinity;
    
    while( right < nums.length){
      
        minDiff = Math.min(minDiff, nums[right] - nums[left]);
        left++;
        right++;
    }
    
    return minDiff;
};