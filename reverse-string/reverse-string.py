'''
Data Types: integer, float, double, string, char
constant: 5
​
int a = 5           (variable a is type of integer)
float b = 5.0      (float, double)
char c = 'h'        (char)
string x = 'hello'  (string)
​
Loops:
​
print('ali')
​
'''
​
#s = ["h","e","l","l","o"]
# r = ["o","l","l","e","h"]
​
 #   0     1   2   3    4
#s = ["o","l","l","e","h"]
            # s[left] = s[left] + s[right]
            # s[left] = s[left] - s[right]    
            # s[right] = s[left] - s[right]
            #s[left], s[right] = s[right], s[left]
            
            # O(n/2)
            
​
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1  
​
        while( left < right):
            temp = s[left]          # temp = e
            s[left] = s[right]      # s[1] =s[3],   l
            s[right] = temp         # S[3]  = temp, e 
            left += 1               # left = 2
            right -= 1              # right = 2
​
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
