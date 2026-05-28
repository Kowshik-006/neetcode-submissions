class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = set()
        nums.sort()
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        output.add(tuple([nums[i], nums[j], nums[k]]))

        return [list(i) for i in output]