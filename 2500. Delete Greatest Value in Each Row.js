// You are given an m x n matrix grid consisting of positive integers.

// Perform the following operation until grid becomes empty:

// Delete the element with the greatest value from each row. If multiple such elements exist, delete any of them.
// Add the maximum of deleted elements to the answer.
// Note that the number of columns decreases by one after each operation.

// Return the answer after performing the operations described above.

/**
 * @param {number[][]} grid
 * @return {number}
 */
var deleteGreatestValue = function(grid) {
    let total = 0;

    for(r of grid) {
        r.sort((a,b) => b-a);
    }
    // console.log(grid);

    while(grid[0].length > 0) {
        let max = 0;
        for(r of grid) {
            max = Math.max(max, r.pop());
        }
        total += max;
    }
    // console.log(total);
    return total;
 };
