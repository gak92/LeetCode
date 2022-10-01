/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    let res = [];
    
    for(let count=0; count<2; count++) {
        for(let i=0; i<nums.length; i++) {
            res.push(nums[i]);
        }
    }
    return res;
};