# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right    

class Solution:

    max_length: int = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)

        return self.max_length
        
    
    def dfs(self, node: Optional[TreeNode]):
        if not node:
            return 0
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)

        self.max_length = max(self.max_length, left + right)

        return 1 + max(left, right)
