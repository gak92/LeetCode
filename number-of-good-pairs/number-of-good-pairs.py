class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic = {}
        count = 0
        
        for num in nums:
            if num not in dic:
                dic[num] = 1
            elif num in dic:
                count += dic[num]
                dic[num] += 1
                
        return count
        
        
        
        
        
#         nop = 0
#         for i in range(len(nums)):
#             for j in range(1, len(nums)):
#                 if (nums[i] == nums[j] and i < j):
#                     nop += 1
                    
#         return nop
                    
        
        
        
        
# class Solution {
#     public int numIdenticalPairs(int[] nums) {
        
#         int ans = 0;
#         int[] count = new int[101];
        
#         for(int n: nums)
#             count[n]++;
        
#         for(int n: count)
#             ans += (n * (n - 1))/2;
        
#         return ans;
#     }
# }