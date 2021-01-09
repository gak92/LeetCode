class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)           # no. of rows
        n = len(grid[0])        # no. of cols
​
        summ = [[grid[j][i] for i in range(n)] for j in range(m)]
​
        for i in range(1,n):
            summ[0][i] = summ[0][i-1] + grid[0][i] 
​
        for i in range(1,m):
            summ[i][0] = summ[i-1][0] + grid[i][0]
​
        for i in range(1,m):
            for j in range(1,n):
                summ[i][j] = min(summ[i-1][j], summ[i][j-1]) + grid[i][j]
​
        return summ[m-1][n-1]
        
