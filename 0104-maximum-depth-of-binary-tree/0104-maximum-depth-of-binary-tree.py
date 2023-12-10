# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # node none, return 0
        if not root:
            return 0
        
        #max depth of the left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # max depth among left and right subtrees, plus 1 for the current node
        return max(left_depth, right_depth) + 1
