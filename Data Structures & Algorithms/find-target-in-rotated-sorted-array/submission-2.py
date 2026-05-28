class Solution:
    def binarySearch(self, nums:List[int], left:int, right:int, target:int)->int:
        while left <= right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                return mid
            else:
                right = mid - 1
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        mid = 0
        right = len(nums)-1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left

        result = self.binarySearch(nums,0,pivot-1,target)
        
        return result if result != -1 else self.binarySearch(nums,pivot,len(nums)-1,target)
        
