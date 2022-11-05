/**
 * @param {number[][]} points
 * @return {number}
 */
var minTimeToVisitAllPoints = function(points) {
    let diff = 0;
    let time = 0;
    
    for(let i=0; i<points.length-1; i++)
    {
        let prev = points[i];
        let curr = points[i+1];
        
        diff = Math.max(Math.abs(curr[0] - prev[0]), Math.abs(curr[1] - prev[1]));
        time += diff;
        // console.log(diff);
    }
    
    // console.log(time);
    return time;
};