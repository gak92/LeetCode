class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0

        for i in range(n):
            res += (((i+1) * (n-i)+1)//2 ) * arr[i]
            
        return res