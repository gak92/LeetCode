class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        length = len(letters)
        if(target >= letters[length-1] or target < letters[0]):
            return letters[0]
        
        left = 0
        right = length - 1
        
        while(left<=right):
            mid = left + (right - left) // 2
            
            if(letters[mid] > target):
                right = mid -1
            else:
                left = mid + 1
                
        return letters[left]
