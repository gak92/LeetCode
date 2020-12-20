# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
​
    def __init__(self, root: TreeNode):
        self.stack = []
        self.helper(root)
        
​
        
    def helper(self, root):
        while(root):
            self.stack.append(root)
            root = root.left
        
        
    def next(self) -> int:
        top_most = self.stack.pop()
        if top_most.right:
            self.helper(top_most.right)
        return top_most.val
        
​
    def hasNext(self) -> bool:
        if len(self.stack) > 0:
            return True
        return False
        
​
​
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
​
​
​
​
​
​
​
​
​
'''
​
class BSTIterator {
public:
    vector<int> tree;
    int counter = 0;
    BSTIterator(TreeNode* root) {
        dfs(root);
    }
    void dfs(TreeNode* root){
        if(!root)return;
        dfs(root->left);
        tree.push_back(root->val);
        dfs(root->right) ;
    }
    int next() {
        int x = tree[counter];
        counter++;
        return x;
    }
    bool hasNext() {
        if(counter < tree.size())
            return true;
        else return false;
    }
};
​
​
​
'''
