class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        length = 0
        max_length = -1

        for i in range(len(s)):
            if s[i] in last_seen:
                max_length = max(max_length, length)
                length = min(length+1, i - last_seen[s[i]])
                last_seen[s[i]] = i
            else:
                length += 1
                last_seen[s[i]] = i
        
        return max(max_length, length)