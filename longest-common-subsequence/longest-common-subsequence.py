class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)
        dp = [[0] * (l2+1) for _ in range(l1+1)]    # create 2d array with 0 values
        # print(dp)
        
        for i, ch1 in enumerate(text1):
            for j, ch2 in enumerate(text2):
                if ch1 == ch2:                      # if character match add 1
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
                    
        return dp[-1][-1]      
        
        
        
​
