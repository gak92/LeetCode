class OrderedStream
{
    constructor(n)
    {
        this.pointer = 0;           // 3
        this.list = [];             // ["aaaaa", "bbbbb", "ccccc", "dddddd" , "eeeeee"]
    }
    
    
    insert = (idKey, value) =>       // 4, "dddddd"
    {
        let chunk = [];
        
        this.list[idKey - 1] = value;   // 3 , "dddddd"
        
        while(this.list[this.pointer]) // list[5] == null
        {
            chunk.push(this.list[this.pointer]);
            this.pointer += 1;                  // 5
        }
        
        return chunk;   ["dddddd", "eeeee"]
    }
}

// OrderedStream os = new OrderedStream(5);
// os.insert(3, "ccccc"); // Inserts (3, "ccccc"), returns [].

// os.insert(1, "aaaaa"); // Inserts (1, "aaaaa"), returns ["aaaaa"].

// os.insert(2, "bbbbb"); // Inserts (2, "bbbbb"), returns ["bbbbb", "ccccc"].

// os.insert(5, "eeeee"); // Inserts (5, "eeeee"), returns [].

// os.insert(4, "ddddd"); // Inserts (4, "ddddd"), returns ["ddddd", "eeeee"].



// /**
//  * @param {number} n
//  */
// var OrderedStream = function(n) {
    
// };

// /** 
//  * @param {number} idKey 
//  * @param {string} value
//  * @return {string[]}
//  */
// OrderedStream.prototype.insert = function(idKey, value) {
    
// };

// /** 
//  * Your OrderedStream object will be instantiated and called as such:
//  * var obj = new OrderedStream(n)
//  * var param_1 = obj.insert(idKey,value)
//  */