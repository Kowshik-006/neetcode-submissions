class Solution:
    def isValid(self, s: str) -> bool:
        bkt = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        stack = []

        for c in s: 
            if c in bkt.keys():
                stack.append(c)
            else:
                if len(stack) == 0 or bkt[stack.pop()] != c :
                    return False
        if len(stack) != 0:
            return False
        
        return True