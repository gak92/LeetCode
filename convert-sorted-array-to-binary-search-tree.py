# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        head = helper(nums, 0, len(nums))
        return head
​
def helper(nums, start, end):
    if start == end:
        return None
    
    mid = (start + end) // 2
    node = TreeNode(nums[mid])
    node.left = helper(nums, start, mid)
    node.right = helper(nums, mid+1, end)
​
    return node   
