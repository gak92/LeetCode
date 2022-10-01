/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    let top = 0;
    let bottom = matrix.length-1;
    let left = 0;
    let right = matrix[0].length-1;
    let i;
    let totalElement = (bottom+1) * (right+1);
    let count = 0;
    let res = [];
    
    while (count < totalElement)
    {
        for (i=left; i<=right && count < totalElement; i++) {
            res.push(matrix[top][i]);
            count += 1;
        }
        top += 1;
        for (i=top; i<=bottom && count < totalElement; i++) {
            res.push(matrix[i][right]);
            count += 1;
        }
        right -=1;
        for (i=right; i>=left && count < totalElement; i--) {
            res.push(matrix[bottom][i]);
            count += 1;
        }
        bottom -=1;
        for (i=bottom; i>=top && count < totalElement; i--) {
            res.push(matrix[i][left]);
            count += 1;
        }
        left +=1;
    }
    
    return res;
};