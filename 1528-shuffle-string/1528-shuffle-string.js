/**
 * @param {string} s
 * @param {number[]} indices
 * @return {string}
 */
var restoreString = function(s, indices) {
    let map = new Map();
    let str = "";
    
    for(let i=0; i<indices.length; i++)
    {
        map.set(indices[i], s[i]);
    }
    
    for(let i=0; i<indices.length; i++)
    {
        str += map.get(i);
    }
    return str;
    
//     let str = [];
    
//     for(let i=0; i<indices.length; i++)
//     {
//         str[indices[i]] = s[i];
//     }
    
//     // console.log(str.join(""));
//     return str.join("");
};