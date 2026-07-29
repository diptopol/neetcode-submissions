# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    isBal: bool 

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBal = True

        self.traverseTree(root)

        return self.isBal


    def traverseTree(self, node: Optional[TreeNode]):
        if not node:
            return 0

        leftHeight = self.traverseTree(node.left)
        rightHeight = self.traverseTree(node.right)

        if abs(leftHeight - rightHeight) > 1:
            self.isBal = False
        
        return 1 + max(leftHeight, rightHeight)
