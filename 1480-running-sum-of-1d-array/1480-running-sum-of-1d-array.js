/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
//     let res = [];
    
//     for(let i=0; i<nums.length; i++) {
//         if(i==0) {
//             res.push(nums[i]);
//         }
//         else{
//             res.push(nums[i] + res[i-1]);    
//         }
//     }
    
    for(let i=1; i<nums.length; i++) {
        nums[i] += nums[i-1];
    }
    console.log(nums);

    return nums;
};