class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        for i in range(1,len(height)-1):
            left_max = right_max = height[i]
            
            for j in range(0,i):
                left_max = max(left_max,height[j])
            
            for j in range(i+1,len(height)):
                right_max = max(right_max, height[j])
            
            area += min(left_max,right_max) - height[i]

        return area