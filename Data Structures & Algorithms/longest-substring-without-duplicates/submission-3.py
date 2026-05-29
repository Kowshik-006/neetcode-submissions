class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_d = defaultdict(list)
        max_length = 0
        length = 0
        for i,c in enumerate(s):
            if c in seen_d:
                length = min(length+1, i - seen_d[c][0])
                seen_d[c] = [i,length]
                max_length = max(max_length, length)
            else:
                length += 1
                seen_d[c] = [i,length]
                max_length = max(max_length, length)
        
        return max_length