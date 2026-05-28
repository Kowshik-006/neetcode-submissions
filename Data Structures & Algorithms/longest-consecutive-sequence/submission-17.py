class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        
        nums.sort()
        length = 1
        lengths = []
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                length += 1
            elif nums[i] - nums[i-1] > 1:
                lengths.append(length)
                length = 1
            if i == len(nums) - 1:
                lengths.append(length)

        return max(lengths)