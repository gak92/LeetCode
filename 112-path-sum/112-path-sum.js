/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} targetSum
 * @return {boolean}
 */

let dfs = (root, targetSum) => {
    if(root === null)
        return false;
    
    if(root.left === null && root.right === null)
        return root.val === targetSum;
    
    let leftTree = dfs(root.left, targetSum-root.val);
    let rightTree = dfs(root.right, targetSum-root.val);
    
    return leftTree || rightTree;
}

var hasPathSum = function(root, targetSum) {
    return dfs(root, targetSum);
};