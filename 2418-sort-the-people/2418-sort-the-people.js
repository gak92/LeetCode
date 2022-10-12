/**
 * @param {string[]} names
 * @param {number[]} heights
 * @return {string[]}
 */
var sortPeople = function(names, heights) {
    
    const map = new Map();
    let res = [];
    
    heights.forEach((height, i) => map.set(height, names[i]));
    heights.sort((a,b) => b-a);
    heights.forEach((height) => res.push(map.get(height)));
    
    return res;
    
//     for(let i=0; i<names.length; i++)
//     {
//         for(let j=i+1; j<heights.length; j++)
//         {
//             if(heights[j]>heights[i])
//             {
//                 let temp = heights[j];
//                 heights[j] = heights[i];
//                 heights[i] = temp;
//                 let temp2 = names[j];
//                 names[j] = names[i];
//                 names[i] = temp2;
//             }
//         }
        
//     }
    
    // return names;
};
