class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        dp = [-1] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        print(dp)
        
        def trib(n):
            if n<3:
                return dp[n]
            
            if dp[n] != -1:
                return dp[n]
            
            dp[n] = trib(n-1) + trib(n-2) + trib(n-3)
            
            return  dp[n] 
        
        print(dp)
        return trib(n)
    
    
    
    
    
    
    
    
    
    
   # hmap = {0: 0, 1: 1, 2: 1}
   #      def trib(n):
   #          if n in hmap:
   #              return hmap[n]
   #          else:
   #              value = trib(n-1) + trib(n-2) + trib(n-3)
   #              hmap[n] = value
