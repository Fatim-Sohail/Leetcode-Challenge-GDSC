class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            # Calculate the area between the two lines
            h = min(height[left], height[right])
            w = right - left
            area = h * w

            # Update the maximum area if the current area is larger
            max_area = max(max_area, area)

            # Move the pointers based on the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area