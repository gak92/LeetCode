/**
 * @param {number[][]} items1
 * @param {number[][]} items2
 * @return {number[][]}
 */
var mergeSimilarItems = function(items1, items2) {
    let map = new Map();
    
    for(let [val, wt] of items1.concat(items2))
    {
        if(map.has(val))
        {
            map.set(val, map.get(val) + wt);
        }
        else
        {
            map.set(val, wt);
        }
    }
    
    let res = Array.from(map.entries());
    res.sort((a,b) => a[0] - b[0]);
    return res;
    
};

