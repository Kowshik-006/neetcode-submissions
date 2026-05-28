class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        d = {"(" : ")", "{" : "}", "[" : "]"}

        for c in s:
            if c in d.keys():
                stack.append(c)
            else:
                if len(stack) == 0 or c != d[stack.pop()]:
                    return False
        
        if len(stack) > 0:
            return False
        
        return True