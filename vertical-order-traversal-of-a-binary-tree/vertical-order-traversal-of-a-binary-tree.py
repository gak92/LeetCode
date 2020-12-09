# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        res = []
        if(root == None):
            return res
        cache = {}
        self.min_col, self.max_col = 0, 0
        
        def dfs(node, r, c):
            if(node == None):
                return
            if(c in cache):
                cache[c].append([r, node.val])
            else:
                cache[c] = [[r, node.val]]
            self.min_col = min(self.min_col, c)
            self.max_col = max(self.max_col, c)
            dfs(node.left, r+1, c-1)
            dfs(node.right, r+1, c+1)
            
            
            
        dfs(root, 0, 0)
        for col in range(self.min_col, self.max_col+1):
            col = sorted(cache[col], key = lambda x: (x[0], x[1]))
            print(col)
            col_sorted = []
            for p in col:
                col_sorted.append(p[1])
            res.append(col_sorted)
            
