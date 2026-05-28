class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1

        max_area = -1

        while left < right:
            area = 0
            if heights[left] <= heights[right]:
                area = heights[left] * (right-left)
                max_area = max(area,max_area)
                left += 1
            else:
                area = heights[right] * (right-left)
                max_area = max(area,max_area)
                right -= 1

        return max_area
