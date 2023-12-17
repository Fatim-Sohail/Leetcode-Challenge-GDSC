# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # check if two subtrees are mirror images
        def isMirror(left, right):
            # Base case: If both nodes are None, they are symmetric
            if not left and not right:
                return True
            # If one of the nodes is None and the other is not, they are not symmetric
            if not left or not right:
                return False
            # Check if values are equal and their subtrees are symmetric
            return (left.val == right.val) and isMirror(left.left, right.right) and isMirror(left.right, right.left)

        # Check if the entire tree is symmetric
        return isMirror(root, root)
