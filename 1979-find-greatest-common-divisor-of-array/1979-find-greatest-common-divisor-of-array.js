/**
 * @param {number[]} nums
 * @return {number}
 */
var findGCD = function(nums) {
    let mn = nums[0];
    let mx = nums[0];
    let gcd = 0;
    
    for(let i=1; i<nums.length; i++)
    {
        if(nums[i] < mn)
        {
            mn = nums[i];
        }
        if(nums[i] > mx)
        {
            mx = nums[i];
        }
    }
    console.log(mn, mx);
    
    for(let i=mn; i>0; i--)
    {
        if(mn%i== 0 && mx%i==0)
        {
            gcd = i;
            break;
        }
    }
    console.log(gcd);
    
    return gcd;
};