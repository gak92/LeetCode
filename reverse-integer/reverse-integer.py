class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        
        if(x<0):
            neg = True
            x = x * (-1)
            
        reverse = 0
        
        while(x>0):
            reverse = (reverse * 10) + (x % 10)
            x = floor(x / 10)
​
        if(reverse > pow(2,31)-1):
            return 0
        if(neg):
            return reverse * (-1)
        else:
            return reverse
