/**
 * @param {string[]} words
 * @return {number}
 */
var uniqueMorseRepresentations = function(words) {
    let letters = 'abcdefghijklmnopqrstuvwxyz';
    let morseCodes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."];
    let map = new Map(morseCodes.map((code, index) => [letters[index], code]))
    // console.log(map);
    
    let set = new Set();
    
    words.forEach((word) => {
        let res = '';
        for(let i=0; i<word.length; i++)
        {
            res += map.get(word[i]);
        }
        
        if(!set.has(res))
        {
            set.add(res);
        }
    });
    
    return set.size;
    
};