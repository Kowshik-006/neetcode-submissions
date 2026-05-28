class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,n in enumerate(nums):
            diff = target - n
            if n in hashmap:
                return [hashmap[n], i]
            else:
                hashmap[diff] = i
        return []
