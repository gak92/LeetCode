class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        
        even = 0
        odd = 1
        
        for i in nums:
            if i % 2 == 0:
                ans[even] = i
                even += 2
            else:
                ans[odd] = i
                odd += 2
                
        return ans