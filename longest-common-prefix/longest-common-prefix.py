class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        base = strs[0]
        
        for i,w in enumerate(strs):
            if(len(w) < len(base)):
                base = w
        strs.remove(base)
        ln = len(base)
        prefix = ''
​
        for i in range(0,ln):
            for w in strs:
                if(w[i] != base[i]):
                    break
            if(w[i]!=base[i]):
                break
            prefix = prefix + base[i]
            
        return prefix
​
