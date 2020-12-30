class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits) -1
        digits[l] += 1
        for i in range(l, -1, -1):
            if digits[i] == 10:
                digits[i] = 0
                if i == 0:
                    digits[:0] = [1]    # insert at the begining of list
                else:
                    digits[i-1] += 1 
​
        return digits
