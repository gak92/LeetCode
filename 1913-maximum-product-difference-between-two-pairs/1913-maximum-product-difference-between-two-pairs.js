/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProductDifference = function(nums) {
    let sortedNums = nums.sort((a,b) => a-b);
    
    let res = (sortedNums[nums.length-1]*sortedNums[nums.length-2]) - (sortedNums[0]*sortedNums[1]);
    return res;
};