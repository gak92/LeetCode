class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        
        for index, num in enumerate(nums):
            if num in mydict:
                return [mydict[num], index]
            else:
                mydict[target-num] = index
