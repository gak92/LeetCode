class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        def isMagic(a,b,c,d,e,f,g,h,i):
            s1 = set([a,b,c,d,e,f,g,h,i])
            s2 = set([1,2,3,4,5,6,7,8,9])
            r1 = a+b+c
            r2 = d+e+f
            r3 = g+h+i
            c1 = a+d+g
            c2 = b+e+h
            c3 = c+f+i
            d1 = a+e+i
            d2 = c+e+g
            if((s1 == s2) and (r1 == r2 == r3 == c1 == c2 == c3 == d1 == d2 == 15)):
                print(r1,r2,r3,c1,c2,c3,d1,d2)
                return True            
            return False
        
        res = 0
        for r in range(0,row-2):
            for c in range(0, col-2):
                if(grid[r+1][c+1] != 5):
                    continue
                if(isMagic(grid[r][c], grid[r][c+1], grid[r][c+2],
                           grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2],
                           grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2])):
                    res +=1
                    
        return res
                
