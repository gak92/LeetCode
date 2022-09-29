/**
 * @param {number[]} nums
 * @param {number[]} index
 * @return {number[]}
 */
var createTargetArray = function(nums, index) {
    let len = nums.length;
    let res = [];
    
    for (let i=0; i<len; i++){                  // len = 5
        res[i] = -1;   
    }
    
    for (let i=0; i<len; i++) {                 // i=0, 1, 2, 3
                
        if (res[index[i]] === -1) {             // index[0]=0, index[1]=1, index[2]=2, index[2]=2, res[2]!==-1
            res[index[i]] = nums[i];            // res[0] = 0, res[1] = 1, res[2] =2
        }
        else{
            for (j=len-1; j>=index[i]; j--){      // j=3, j>=2
                res[j] = res[j-1];
            }
            res[index[i]] = nums[i];
        }   
    }
    return res;
        
};