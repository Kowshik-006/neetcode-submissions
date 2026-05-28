class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = -1
        for i in range(len(heights)):
            left = 0
            right = 0
            for j in range(i-1,-1,-1):
                if heights[j] >= heights[i]:
                    left += 1
                else:
                    break
            
            for j in range(i+1, len(heights)):
                if heights[j] >= heights[i]:
                    right += 1
                else:
                    break
            
            area = (left + right + 1) * heights[i]
            max_area = max(area, max_area)

        return max_area
        