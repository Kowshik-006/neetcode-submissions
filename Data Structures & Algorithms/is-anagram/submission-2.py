class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_s = defaultdict(int)
        map_t = defaultdict(int)

        for i in range(len(s)):
            map_s[s[i]] += 1
            map_t[t[i]] += 1

        for key, value in map_s.items():
            if map_t[key] != value:
                return False

        return True