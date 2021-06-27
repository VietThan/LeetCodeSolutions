# Python 3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count  = 1
        
        def dfs(node, maxVal):
            
            nonlocal count
            
            if node:
            
                if node.val >= maxVal:
                    count += 1
            
                if node.left:
                    dfs(node.left, max(node.val, maxVal))
                
                if node.right:
                    dfs(node.right, max(node.val, maxVal))
                
        dfs(root.left, root.val)
        dfs(root.right, root.val)
        
        return count
