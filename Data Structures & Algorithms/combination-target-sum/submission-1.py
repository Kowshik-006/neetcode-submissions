class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, currList, total):
            if total == target:
                res.append(currList.copy())
                return 

            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                
                currList.append(nums[j])
                dfs(j, currList, total + nums[j])
                currList.pop()
            
        dfs(0, [], 0)

        return res