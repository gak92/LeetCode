# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         res = []                                    # resultant list of list
#         q = []                                      # initialize queue
        
#         if(root == None):                           # if no element then return res
#             return res
#         q.append(root)                              # if ele, then put it in q
        
#         while(q):                                   # run loop until something in it
#             qsize = len(q)                          # get size of q
#             curr = []                               # create temp list
#             for i in range(qsize):                  # run loop till size of q
#                 temp = q.pop(0)                     # pop item from q and store in temp
#                 if(temp.left):                      # if something in left of temp, push it in q
#                     q.append(temp.left)
#                 if(temp.right):                     # if something in right of temp, push it in q
#                     q.append(temp.right)
                    
#                 curr.append(temp.val)               # push ele of temp in curr list
                
#             res.append(curr)                        # after for loop, push entire curr list into res
#         return res                                  # return result after end of while loop
        
        
        
        res = []                                    # resultant list of list
        q = deque()                                 # initialize queue
        
        if(root == None):                           # if no element then return res
            return res
        q.append(root)                              # if ele, then put it in q
        
        while(q):                                   # run loop until something in it
            qsize = len(q)                          # get size of q
