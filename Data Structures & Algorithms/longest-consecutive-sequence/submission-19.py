class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 or n == 1:
            return n
        
        nums.sort()

        length = 1
        max_length = 1

        for i in range(1,n):
            if nums[i] == nums[i-1] + 1:
                length += 1
            elif nums[i] - nums[i-1] > 1:
                max_length = max(max_length, length)
                length = 1

        return max(max_length, length)
        