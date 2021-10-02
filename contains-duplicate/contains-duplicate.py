class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniq = {}
        
        for i,val in enumerate(nums):
            if val in uniq:
                return True
            else:
                uniq[val] = 1
                
        return False