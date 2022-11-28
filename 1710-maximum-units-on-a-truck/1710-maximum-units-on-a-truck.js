/**
 * @param {number[][]} boxTypes
 * @param {number} truckSize
 * @return {number}
 */
var maximumUnits = function(boxTypes, truckSize) {
    boxTypes.sort((a,b) => b[1]-a[1]);
    // console.log(boxTypes);
    
    let totalUnits = 0;
    for(let box of boxTypes)
    {
        let numOfBoxes = Math.min(truckSize, box[0]);
        // console.log("Min val is: ", numOfBoxes);
        totalUnits += numOfBoxes * box[1];
        truckSize -= numOfBoxes;
    }
    
    return totalUnits;
};
