class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 or n == 1:
            return n
            
        nums_set = set(nums)
        max_length = -1
        for num in nums_set:
            if num - 1 not in nums_set:
                length = 1
                while num + 1 in nums_set:
                    length += 1
                    num += 1
                
                max_length = max(max_length, length)

        return max_length
