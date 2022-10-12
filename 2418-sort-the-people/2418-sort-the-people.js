/**
 * @param {string[]} names
 * @param {number[]} heights
 * @return {string[]}
 */
var sortPeople = function(names, heights) {
    
    for(let i=0; i<names.length; i++)
    {
        // let max = heights[i];
        // let maxidx = i;
        for(let j=i+1; j<heights.length; j++)
        {
            if(heights[j]>heights[i])
            {
                let temp = heights[j];
                heights[j] = heights[i];
                heights[i] = temp;
                let temp2 = names[j];
                names[j] = names[i];
                names[i] = temp2;
            }
        }
        
    }
    
    return names;
};