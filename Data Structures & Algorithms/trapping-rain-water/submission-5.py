class Solution:
    def trap(self, height: List[int]) -> int:
        area = [0] * len(height)

        for i in range(1,len(height)-1):
            left_max = 0
            
            for j in range(0,i):
                left_max = max(left_max,height[j])
            
            right_max = 0

            for j in range(i+1,len(height)):
                right_max = max(right_max, height[j])
            
            area[i] = max(0, min(left_max,right_max) - height[i])

        area_sum = 0
        for i in area:
            area_sum += i

        return area_sum