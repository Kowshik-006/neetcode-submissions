class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] =  How many ways to decode the string: s[i:]
        # Empty string can be decoded in 1 way
        # It indicates we have traversed the entire string
        dp = {len(s) : 1}

        # How many ways to decode the string: s[i:]
        def dfs(i):
            if i in dp:
                return dp[i]
            # If the 1st character is '0', the substring cannot be decoded
            if s[i] == '0':
                return 0

            # take the ith character, let's see how many ways the substring s[i+1:] 
            # can be decoded
            res = dfs(i+1)
            
            # if two characters can be grouped
            if i < len(s)-1:
                # 10 to 26
                if (s[i] == '1' or (s[i] == '2' and s[i+1] <= '6')):
                    # group i and i+1 th character
                    # see how many ways s[i+2:] can be decoded
                    res += dfs(i+2)
            dp[i] = res
            return res

        return dfs(0)