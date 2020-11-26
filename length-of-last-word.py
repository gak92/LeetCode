class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt = 0
        tail = len(s) - 1
        
        while (tail >= 0 and s[tail] == ' '):           # to handle: "a "
            tail -= 1
            
        while (tail >=0 and s[tail] != ' '):
            cnt += 1
            tail -= 1
        
        
        return cnt
