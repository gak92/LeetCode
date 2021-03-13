class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        
        for i in range(len(nums)):
            single ^= nums[i]
            
        return single
        
        
#         single = defaultdict(int)
#         for num in nums:
#             single[num] += 1
            
#         for num in single:
#             if single[num] == 1:
#                 return num
            