class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        nums.sort()
        for i, num in enumerate(nums):
            if num > 0:
                continue
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = n - 1 

            while left < right:
                if num + nums[left] + nums[right] < 0:
                    left += 1
                elif num + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    output.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1

        return output