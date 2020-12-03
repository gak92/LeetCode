# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        #res = []                                    # resultant list of list
        q = deque()                                 # initialize queue
        
        if(root == None):                           # if no element then return res
            return res
        q.append(root)                              # if ele, then put it in q
        max_sum = -32768
        level = 1
        max_sum_level = 0
        
        while(q):                                   # run loop until something in it
            qsize = len(q)                          # get size of q
            curr_sum = 0
            curr = []                               # create temp list
            for i in range(qsize):                  # run loop till size of q
                temp = q.popleft()                     # pop item from q and store in temp
                if(temp.left):                      # if something in left of temp, push it in q
                    q.append(temp.left)
                if(temp.right):                     # if something in right of temp, push it in q
                    q.append(temp.right)
                    
                curr_sum += temp.val 
                #curr.append(temp.val)               # push ele of temp in curr list
                
            #res.append(curr)                        # after for loop, push entire curr list into res
            if curr_sum > max_sum:
                max_sum_level = level
            max_sum = max(curr_sum, max_sum)
            level += 1
        
        return max_sum_level                                  # return result after end of while loop
        
