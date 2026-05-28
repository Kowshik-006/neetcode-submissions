class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = -1
        n = len(heights)
        stack = [] # [start_idx, height] pairs
        for i in range(n):
            start = i
            while len(stack) != 0 and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                area = height * (i - index)
                max_area = max(area, max_area)
                start = index
            stack.append([start,heights[i]])
        
        for i,h in stack:
            area = h * (n-i)
            max_area = max(area, max_area)

        return max_area
