# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        #Sort intervals based on their start times
        intervals.sort(key=lambda x: x[0])

        #Merge overlapping intervals
        merged_intervals = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] <= merged_intervals[-1][1]:
                # Merge overlapping intervals
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
            else:
                # Add non-overlapping interval to the result
                merged_intervals.append(interval)

        return merged_intervals
