class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int count = 0;
        int maxcount = 0;
        int len = nums.size();
        
        for(int i=0; i<len; i++){
            if(nums[i] == 1){
                count++;
                maxcount = max(count, maxcount);
                    
            }
            else{
                count = 0;
            }
        }
        
        return maxcount;
    }
};
