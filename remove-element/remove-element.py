class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        #print(length)
        for i in range(length):
            if val in nums:
                nums.remove(val)
        #print(nums)
        return len(nums)
​
​
