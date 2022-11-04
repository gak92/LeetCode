/**
 * @param {number[][]} image
 * @return {number[][]}
 */
var flipAndInvertImage = function(image) {
    
    for(let i=0; i<image.length; i++)
    {
        let j = 0;
        let k = image[i].length-1;
        // console.log(j,k);
        
        while(j<=k)
        {
            let temp = image[i][j];
            image[i][j] = image[i][k];
            image[i][k] = temp;
            j += 1;
            k -=1
        }
    }
    // console.log(image);
    for(let i=0; i<image.length; i++)
    {
        for(let j=0; j<image[i].length; j++)
        {
            if(image[i][j] === 0)
                image[i][j] = 1;
            else
                image[i][j] = 0;
        }
    }
    
    // console.log(image);
    return image;
};