/**
 * @param {string} s
 * @return {string}
 */
var sortSentence = function(s) {
    let wordsList = s.split(' ');
    // console.log(wordsList);
    
    let hash = {};
    for(let word of wordsList)
    {
        let idx = word[word.length-1];
        let w = word.substr(0, word.length-1);
        // console.log(idx, w);
        hash[idx] = w;
    }
    // console.log(hash);
    
    let res = [];
    
    for(let i=1; i<=wordsList.length; i++)
    {
        res.push(hash[i]);   
    }
    // console.log(res);
    
    return res.join(' ');
};