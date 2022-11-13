/**
 * @param {string} s
 * @return {string}
 */
var toLowerCase = function(s) {
    let lower = "";
    
    for(let i=0; i<s.length; i++)
    {
      // console.log(s[i], " -- " ,s.charCodeAt(i)); 
        let code = s.charCodeAt(i);
        if(code >= 65 && code <= 90)
        {
            code += 32;
            let ch = String.fromCharCode(code);
            lower += ch;
        }
        else
        {
            lower += s[i];
        }
    }
    console.log(lower);
    return lower;
};