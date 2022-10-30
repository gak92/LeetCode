/**
 * @param {string[]} word1
 * @param {string[]} word2
 * @return {boolean}
 */
var arrayStringsAreEqual = function(word1, word2) {
    let wp1 = 0, wp2 = 0;
    let sp1 = 0, sp2 = 0;
    
    while(wp1 < word1.length && wp2 < word2.length)
    {
        if(word1[wp1][sp1] !== word2[wp2][sp2])
            return false;
        sp1 += 1;
        sp2 += 1;
        
        if(sp1 === word1[wp1].length)
        {
            wp1 += 1;
            sp1 = 0;
        }
        if(sp2 === word2[wp2].length)
        {
            wp2 += 1;
            sp2 = 0;
        }
        
    }
    
    return wp1 === word1.length && wp2 === word2.length;
    
};