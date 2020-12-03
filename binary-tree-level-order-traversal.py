# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        q = []
        
        if(root == None):
            return res
        q.append(root)
        
        while(q):
            qsize = len(q)
            curr = []
            for i in range(qsize):
                temp = q.pop(0)
                if(temp.left):
                    q.append(temp.left)
                if(temp.right):
                    q.append(temp.right)
                    
                curr.append(temp.val)
                
            res.append(curr)
        return res
        
        
