class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map_s = defaultdict(int)
        map_t = defaultdict(int)

        for c in s:
            map_s[c] += 1
        
        for c in t:
            map_t[c] += 1

        for c in map_s.keys():
            if c not in map_t or map_s[c] != map_t[c]:
                return False
        return True