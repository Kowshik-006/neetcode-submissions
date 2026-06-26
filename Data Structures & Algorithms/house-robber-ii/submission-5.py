class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        
        def helper(houses):
            for i in range(2,len(houses)):
                if i == 2:
                    houses[i] = houses[i] + houses[i-2]
                else:
                    houses[i] = houses[i] + max(houses[i-2],houses[i-3])
            
            return max(houses[-1],houses[-2])
        
        return max(helper(nums[1:]),helper(nums[:-1]))