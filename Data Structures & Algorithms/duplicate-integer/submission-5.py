class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq = set()

        for i in range(len(nums)):
            if nums[i] in uniq:
                return True
            else:
                uniq.add(nums[i])
        return False