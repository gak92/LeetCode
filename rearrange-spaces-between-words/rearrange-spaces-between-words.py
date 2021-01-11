class Solution:
    def reorderSpaces(self, text: str) -> str:
        if (len(text) == 0):
            return ""
        n_spaces = text.count(" ")
        words = text.split()
        n_words = len(words)
        
        if n_words == 1:
            return words[0] + " " * n_spaces
        
        div = n_spaces // (n_words-1)
        mod = n_spaces % (n_words-1)
        separator = " " * div
        res = separator.join(words) + " " * mod
        return res 
