/**
 * @param {string[][]} items
 * @param {string} ruleKey
 * @param {string} ruleValue
 * @return {number}
 */

let counter = (items, ruleValue, idx) =>
{
    let count = 0;
    for(let i=0; i<items.length; i++)
    {
        if(items[i][idx] == ruleValue)
        {
            count++;
        }
    }
    return count;
}

var countMatches = function(items, ruleKey, ruleValue) {
    // let res = [];
    let count = 0;
    
    if(ruleKey == 'type')
    {
        count = counter(items, ruleValue, 0);   
    }
    else if(ruleKey == 'color')
    {
        count = counter(items, ruleValue, 1);
    }
    else if(ruleKey == 'name')
    {
        count = counter(items, ruleValue, 2);    
    }

    // console.log(res);
    // console.log(count);
    return count;
};