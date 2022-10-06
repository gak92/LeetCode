/**
 * @param {string[][]} items
 * @param {string} ruleKey
 * @param {string} ruleValue
 * @return {number}
 */
var countMatches = function(items, ruleKey, ruleValue) {
    let res = [];
    let count = 0;
    
    if(ruleKey == 'type')
    {
        for(let i=0; i<items.length; i++)
        {
            if(items[i][0] == ruleValue)
            {
                res.push(items[i]);
                count++;
            }
        }
    }
    if(ruleKey == 'color')
    {
        for(let i=0; i<items.length; i++)
        {
            if(items[i][1] == ruleValue)
            {
                res.push(items[i]);
                count++;
            }
        }
    }
    if(ruleKey == 'name')
    {
        for(let i=0; i<items.length; i++)
        {
            if(items[i][2] == ruleValue)
            {
                res.push(items[i]);
                count++;
            }
        }
    }

    console.log(res);
    console.log(count);
    return count;
};