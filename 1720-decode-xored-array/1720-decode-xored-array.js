/**
 * @param {number[]} encoded
 * @param {number} first
 * @return {number[]}
 */
var decode = function(encoded, first) {
    let arr = [];
    
    arr.push(first);
    
    for(let i=0; i<encoded.length; i++)
    {
        let element = arr[i] ^ encoded[i];
        arr.push(element);
    }
    
    return arr;
};