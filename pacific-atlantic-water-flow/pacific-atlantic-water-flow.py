class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        cord = []
        if (len(matrix) == 0):
            return cord
        
        def dfs(matrix, row, col, temp, min_val):
            if(row<0 or col<0 or row>len(matrix)-1 or col>len(matrix[0])-1):
                return
            elif(min_val > matrix[row][col]):
                return
            elif(temp[row][col] == 1):
                return
            
            temp[row][col] = 1
            
            dfs(matrix, row+1, col, temp, matrix[row][col])
            dfs(matrix, row-1, col, temp, matrix[row][col])
            dfs(matrix, row, col+1, temp, matrix[row][col])
            dfs(matrix, row, col-1, temp, matrix[row][col])
​
            
        
        row, col = len(matrix), len(matrix[0])
        pacific = [[0 for x in range(col)] for y in range(row)]
        atlantic = [[0 for x in range(col)] for y in range(row)]
        
​
        MAX_VAL = sys.maxsize
        MIN_VAL = -sys.maxsize - 1
        
        for i in range(0, col):
            dfs(matrix, 0, i, pacific, MIN_VAL)
            
        for i in range(0, row):
            dfs(matrix, i, 0, pacific, MIN_VAL)
            
        for i in range(0, col):
            dfs(matrix, row-1, i, atlantic, MIN_VAL)
            
        for i in range(0, row):
            dfs(matrix, i, col-1, atlantic, MIN_VAL)
            
        for i in range(0, len(pacific)):
