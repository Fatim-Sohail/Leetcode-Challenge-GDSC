from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []  # To store the level order traversal
        queue = deque([root])  # Queue for BFS

        while queue:
            level_values = []  # List to store the values at the current level
            level_size = len(queue)

            for _ in range(level_size):
                current_node = queue.popleft()
                level_values.append(current_node.val)

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

            result.append(level_values)

        return result
