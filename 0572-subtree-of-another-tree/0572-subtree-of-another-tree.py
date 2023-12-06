# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        # Check if the current subtree is identical to subRoot
        if self.isIdentical(root, subRoot):
            return True

        # Recursively check the left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isIdentical(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False

        # Check if the current nodes are equal and recursively check their subtrees
        return (
            root1.val == root2.val
            and self.isIdentical(root1.left, root2.left)
            and self.isIdentical(root1.right, root2.right)
        )