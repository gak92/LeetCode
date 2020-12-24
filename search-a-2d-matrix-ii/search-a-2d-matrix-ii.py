class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)                     # length of row
        if(m == 0):
            return False
        
        n = len(matrix[0])                  # length of column
        
        i = 0                               # initialize 1st row
        j = n-1                             # initialize last column
        
        while(i<m and j>=0):                # while row < # of rows, col >= 1st column
            if matrix[i][j] == target:      # if element found return True
                return True
            
            if matrix[i][j] > target:       # if ele > target, decrease column #
                j -= 1
            else:                           # if ele < target, increase row #
                i += 1
                
        return False
