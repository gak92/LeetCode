/**
 * @param {number[][]} grid
 * @return {number[][]}
 */
var largestLocal = function(grid) {
    let maxLocal = [];
    let maxArray = [];
    let len = grid.length;              // len = 4
    let max;
    
    for (let i=0; i<len-2; i++) 
    {
        maxArray = [];
        for (let j=0; j<len-2; j++) 
        {
            max = getMaxValue(grid, i, j);
            maxArray.push(max);
        }  
        console.log(maxArray);
        maxLocal.push(maxArray);
    }
    return maxLocal;
};

let getMaxValue = function(grid, m, n) {
    let max = grid[m][n];
    
    for (let i=m; i<m+3; i++)
    {
        for (let j=n; j<n+3; j++)
        {
            if (grid[i][j] > max) 
            {
                max = grid[i][j];
            }
        }
    }
    return max;
}