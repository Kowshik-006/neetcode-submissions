class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c)-ord('a')] += 1
            m[tuple(key)].append(s)
        
        return [val for val in m.values()]