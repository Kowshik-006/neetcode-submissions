class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # (value, index) pair

        for i, v in enumerate(temperatures):
            while len(stack) > 0 and v > stack[-1][0]:
                # temp at ind i is greater than the temp at stackInd
                stackVal, stackInd = stack.pop()
                result[stackInd] = i - stackInd
            stack.append([v,i])
        
        return result