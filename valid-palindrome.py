class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0                               # initial index
        r = len(s) - 1                      # last index
        
        while(l < r):
            if(not s[l].isalnum()):
                l += 1
            elif(not s[r].isalnum()):
                r -= 1
            else:
                if(s[l].lower() != s[r].lower()):
                    return False
                l += 1
                r -= 1
                               
        return True
             
        
        
        
        
        
    # l, r = 0, len(s)-1
    # while l < r:
    #     while l < r and not s[l].isalnum():
    #         l += 1
    #     while l <r and not s[r].isalnum():
    #         r -= 1
    #     if s[l].lower() != s[r].lower():
    #         return False
    #     l +=1; r -= 1
    # return True
