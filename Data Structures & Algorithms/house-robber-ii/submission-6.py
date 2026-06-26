class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        
        def helper(houses):
            houses[1] = max(houses[0],houses[1])

            for i in range(2,len(houses)):
                houses[i] = max(houses[i-1], houses[i]+houses[i-2])
            
            return houses[-1]
        
        return max(helper(nums[1:]),helper(nums[:-1]))