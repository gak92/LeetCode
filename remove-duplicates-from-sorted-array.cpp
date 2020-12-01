class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size()==0){
            return 0;
        }
        int idx = 0;
        
        for (int i=1; i<nums.size(); ++i){
            if (nums[i] != nums[idx]){
                idx++;
                nums[idx] = nums[i];
            }
        }
        
        return idx+1;
        
    }
};
​
// slow = 0
//         fast = 1
//         length = len(nums)
        
//         while (fast < length):
//             if nums[fast] == nums[slow]:
//                 fast += 1
//             else:
//                 slow += 1
