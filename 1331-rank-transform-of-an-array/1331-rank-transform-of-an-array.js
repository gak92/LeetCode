/**
 * @param {number[]} arr
 * @return {number[]}
 */
var arrayRankTransform = function(arr) {
    let res = arr.slice();
	res.sort((a,b) => a-b);
    console.log(res);
    let map = new Map();
	
	for (let i = 0; i < res.length; i++) {
		if (map.get(res[i]) === undefined)
    	    map.set(res[i], map.size);
	}
    console.log(map);

	for (let i = 0; i < arr.length; i++) {
		res[i] = map.get(arr[i]) + 1;
	}

	return res
};
