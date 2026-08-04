class Solution:
    def numDecodings(self, s: str) -> int:
        # ways for s[i:]
        dp = 0
        # ways for s[i+1:]
        # right to left traversal
        # for i=len(s)-1 -> dp1 = 1
        dp1 = 1
        # ways for s[i+2:]
        dp2 = 0

        for i in range(len(s)-1,-1,-1):
            if s[i] == '0':
                dp = 0
            else:
                dp = dp1

            if i < len(s)-1 and (s[i] == '1' or (s[i] == '2' and s[i+1] <= '6')):
                dp += dp2
            
            # change dp2 first, so that dp2 is updated to the dp1 value of the past not the dp value
            dp2 = dp1
            dp1 = dp
        
        return dp