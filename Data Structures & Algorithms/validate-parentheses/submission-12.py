class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        d = {"(" : ")", "{" : "}", "[" : "]"}

        for c in s:
            if c in d:
                stack.append(c)
            else:
                if len(stack) > 0 and c == d[stack[-1]]:
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        return True