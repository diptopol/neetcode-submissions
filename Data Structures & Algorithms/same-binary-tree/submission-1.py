# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.nodeCheck(p, q)


    
    def nodeCheck(self, pnode: Optional[TreeNode], qnode: Optional[TreeNode]):
        if not pnode and not qnode:
            return True

        elif (not pnode and qnode) or (pnode and not qnode):
            return False

        else:
            if (pnode.val != qnode.val):
                return False
            
            leftResult = self.nodeCheck(pnode.left, qnode.left)
            rightResult = self.nodeCheck(pnode.right, qnode.right)

            return leftResult and rightResult

        







    