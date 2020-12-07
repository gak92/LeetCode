class Solution:
    def romanToInt(self, s: str) -> int:
        value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        lostr = len(s)
        print('length of string: ', lostr)
        res = 0
        i = 0
        
        while(i < lostr):
            c1 = value[s[i]]
            if (i+1 < lostr):
                c2 = value[s[i+1]]
                if (c1 >= c2):
                    res = res + c1
                    i = i + 1
                else:
                    res = res + c2 - c1
                    i = i + 2
            else:
                res = res + c1
                i = i + 1
        return res  
