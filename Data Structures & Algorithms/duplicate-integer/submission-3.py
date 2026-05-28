class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_arr = sorted(nums)

        for i in range(1,len(sorted_arr)):
            if sorted_arr[i] == sorted_arr[i-1]:
                return True
        return False