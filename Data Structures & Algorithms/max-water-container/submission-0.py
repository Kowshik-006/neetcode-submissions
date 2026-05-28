class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = -1
        for i in range(len(heights)-1):
            for j in range(i+1,len(heights)):
                area = min(heights[i],heights[j])*(j-i)
                if area > max_area:
                    max_area = area
        return max_area
        