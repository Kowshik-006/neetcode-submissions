class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 or n == 1:
            return n
        num_set = set(nums)
        maxlen = 1
        for num in num_set:
            if num-1 not in num_set:
                l = 1
                while num + 1 in num_set:
                    l += 1
                    num += 1
                maxlen = max(l, maxlen)

        return maxlen