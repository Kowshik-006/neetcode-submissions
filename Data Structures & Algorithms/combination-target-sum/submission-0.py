class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, currList, total):
            if total == target:
                # copy is necessay since currList is modified later
                res.append(currList.copy())
                return
            if i == len(nums) or total > target:
                return

            currList.append(nums[i])
            dfs(i, currList, total+nums[i])
            '''
            We will reach here after getting a successful list after inserting the ith element
            or by failing to get one. So, we remove the last element of the list and insert the
            next element (i+1) of the nums list to see if we can get any successful list. 
            '''
            currList.pop()
            dfs(i+1, currList, total)
        
        # We start by inserting the 0th element to an empty list having 0 total
        dfs(0, [], 0)

        return res