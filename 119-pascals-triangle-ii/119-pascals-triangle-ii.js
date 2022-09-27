/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function(rowIndex) {
    
//     let currRow = [];
//     let prevRow = [];
    
//     for (let i=0; i<rowIndex; i++) {
        
//     }
    
    let currRow = [];
    currRow.push(1);
    if (rowIndex == 0) {
        return [1];
    }
    
    let prev = getRow(rowIndex - 1);
    
    for (let i=1; i<prev.length; i++) {
        let curr = prev[i-1] + prev[i];
        currRow.push(curr);
    }
    currRow.push(1);
    
    return currRow;
};