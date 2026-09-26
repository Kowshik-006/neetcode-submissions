class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        maxlen = 0
        for num in num_set:
            if num-1 not in num_set:
                l = 1
                while num + 1 in num_set:
                    l += 1
                    num += 1
                maxlen = max(l, maxlen)

        return maxlen