class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums_set = set(nums)
        max_len = 1
        for num in nums_set:
            if num - 1 not in nums_set:
                len_ = 1
                n = num + 1
                while n in nums_set:
                    len_ += 1
                    n += 1
                max_len = max(max_len, len_)

        return max_len