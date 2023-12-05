class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Sort intervals based on ending points
        intervals.sort(key=lambda x: x[1])

        # Initialize variables
        end = intervals[0][1]
        count = 0

        # Iterate through sorted intervals
        for i in range(1, len(intervals)):
            # Check for overlapping intervals
            if intervals[i][0] < end:
                # Remove overlapping interval with the larger ending point
                count += 1
            else:
                # Update ending point
                end = intervals[i][1]

        return count