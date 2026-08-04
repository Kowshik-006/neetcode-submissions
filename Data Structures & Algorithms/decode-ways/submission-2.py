class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] = number of ways to decode s[i:]
        dp = {len(s) : 1}

        for i in range(len(s)-1,-1,-1):
            # invalid start
            if s[i] == '0':
                dp[i] = 0
            # ith char + all the ways from (i+1)
            # we are basically adding an element on top of each branch from i+1
            else:
                dp[i] = dp[i+1]
            
            if i < len(s)-1 and (s[i] == '1' or (s[i]=='2' and s[i+1]<='6')):
                # (i & i+1) + all the ways from (i+2)
                dp[i] += dp[i+2]
            
        return dp[0]