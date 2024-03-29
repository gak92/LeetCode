/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    let num = 0;
    let values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000};
    
    for(let i=0; i<s.length; i++)
    {
        console.log(values[s[i]]);
        if(values[s[i+1]] > values[s[i]])
        {
            num += values[s[i+1]] - values[s[i]];
            i += 1;
        }
        else
        {
            num += values[s[i]];
        }
    }
    
    console.log(num);
    return num;
    
};