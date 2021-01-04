class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        anchor = 0
        explorer = 0
        l = len(nums)
​
        while(explorer < l):
            if nums[explorer] != 0:
                temp = nums[anchor]
                nums[anchor] = nums[explorer]
                nums[explorer] = temp
                anchor +=1
            explorer +=1
