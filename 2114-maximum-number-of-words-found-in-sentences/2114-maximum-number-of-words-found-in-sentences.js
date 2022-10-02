/**
 * @param {string[]} sentences
 * @return {number}
 */
var mostWordsFound = function(sentences) {
    let max = 0;
    
    for(let i=0; i<sentences.length; i++)
    {
        let sentence = sentences[i].split(" ");
        
        if (sentence.length > max)
        {
            max = sentence.length;
        }
    }
    
    return max;
};