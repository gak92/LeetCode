class Solution:
    def sumZero(self, n: int) -> List[int]:
        l = n//2
        rem = n%2
        
        if rem != 0:
            res = [0]
        else:
            res = []
            
        for i in range(1, l+1):
            res.append(i)
            res.append(-i)
        
        return res
        
        # result = []
        # counter = n
        # if n % 2 != 0:
        #     result.append(0)
        #     counter -= 1
        # while counter > 0:
        #     result.append(counter)
        #     result.append(counter * -1)
        #     counter -= 2
        # return result
        
        