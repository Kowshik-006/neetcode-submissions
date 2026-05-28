class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix = 1
        suffix = 1

        for i in range(len(nums)):
            output.append(prefix)
            prefix *= nums[i]

        for i in range(len(nums)-1,-1,-1):
            output[i] *= suffix
            suffix *= nums[i]

        return output