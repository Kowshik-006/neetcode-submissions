class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_d = defaultdict(int)
        max_length = 0
        length = 0
        for i,c in enumerate(s):
            if c in seen_d:
                max_length = max(max_length, length)
                length = min(length+1, i - seen_d[c])
                seen_d[c] = i
            else:
                length += 1
                seen_d[c] = i
                
        
        max_length = max(max_length, length)
        
        return max_length