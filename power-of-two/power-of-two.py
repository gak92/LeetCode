class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        if n==1:
            return True
        
        while(n!=1):
            rem = n % 2
            if(rem==1):
                return False
            n = n / 2
            
        return True