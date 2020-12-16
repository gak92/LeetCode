class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_paren = ["(", "{", "["]
        
        for char in s:
            if (char in open_paren):
                stack.append(char)
            elif (char == ')' and (stack) and stack[-1] == '('):
                stack.pop()
            elif (char == '}' and (stack) and stack[-1] == '{'):
                stack.pop()
            elif (char == ']' and (stack) and stack[-1] == '['):
                stack.pop()
            else:
                return False
​
        return True if not stack else False
