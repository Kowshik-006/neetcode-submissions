class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = defaultdict(int)

        for index, value in enumerate(nums):
            if (target - value) in nums_dict:
                return [nums_dict[target-value], index]
            else:
                nums_dict[value] = index
        
        return []