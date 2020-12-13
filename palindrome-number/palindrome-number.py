class Solution:
    def isPalindrome(self, x: int) -> bool:
        orig = x
        if(x<0):
            return False
        rev = 0
        while(x > 0):
            rev = (rev * 10) + (x % 10)
            x = math.floor(x / 10)
​
        if(orig == rev):
            return True
        else:
            return False
