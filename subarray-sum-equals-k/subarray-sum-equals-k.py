class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        length = len(nums)
        if (length == 0):
            return 0
        
        curr_sum = 0
        count = 0
        d = {}
        
        for i in range(length):
            curr_sum += nums[i]
            if (curr_sum == k):
                count += 1
                
            if ((curr_sum-k) in d):
                count += d[curr_sum-k]
                
            d[curr_sum] = d.get(curr_sum, 0) + 1
            print("count: ", count)
            
        print(d)
        return count
            