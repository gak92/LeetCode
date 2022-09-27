/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function(rowIndex) {
    
    let res = [];
    
    for (let i=0; i<=rowIndex; i++) {
        res.push([]);
        
        for (let j=0; j<=i; j++) {
            if (j==0 || j==i) {
                res[i][j] = 1;
            }
            else {
                res[i][j] = res[i-1][j-1] + res[i-1][j];
            }
        }
    }
    return res[rowIndex];
    
    
//     let currRow = [];
//     currRow.push(1);
//     if (rowIndex == 0) {
//         return [1];
//     }
    
//     let prev = getRow(rowIndex - 1);
    
//     for (let i=1; i<prev.length; i++) {
//         let curr = prev[i-1] + prev[i];
//         currRow.push(curr);
//     }
//     currRow.push(1);
    
//     return currRow;
};