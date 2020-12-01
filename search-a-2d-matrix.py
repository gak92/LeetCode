class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)                 # m = 1
        if(m == 0):
            return False
        n = len(matrix[0])              # n = 2
        
        lo = 0                          # 0
        hi = m * n -1                   # 1*2 -1 =  1
        
        while(lo <= hi):                    # 0 < 1
            mid = lo + (hi - lo) // 2       # 0 +(1-0)/2 = 0
            val = matrix[mid//n][mid%n]      # matrix[5/4][5%4] = [1][1]
            
            if(val == target):
                return True
            elif(val < target):
                lo = mid + 1
            else:
                hi = mid - 1
                
        return False
                
