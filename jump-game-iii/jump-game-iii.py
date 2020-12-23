class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if start >=0 and start < len(arr) and arr[start] >= 0:      # check out of bound & not visited
            if arr[start] == 0:
                return True
            
            arr[start] = -arr[start]            # -ve means visited
            return self.canReach(arr, start+arr[start]) or self.canReach(arr, start-arr[start])
        
        return False
        
        
