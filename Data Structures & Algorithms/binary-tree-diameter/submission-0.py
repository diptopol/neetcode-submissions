# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right    

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        return self.traverseBTree(root, -1)

    def traverseBTree(self, node: Optional[TreeNode], length):
        if not node:
            return length

        length = length + 1

        lengthLeft = self.traverseBTree(node.left, length)
        lengthRight = self.traverseBTree(node.right, length)
        lengthLeafToLeaf = lengthLeft - length + lengthRight - length

        return max(lengthLeft, lengthRight, lengthLeafToLeaf)
        