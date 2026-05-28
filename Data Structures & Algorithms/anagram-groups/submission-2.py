class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            counts = [0] * 52
            for c in s:
                if ord(c) >= ord('a'):
                    counts[ord(c)-ord('a')] += 1
                else:
                    counts[ord(c)-ord('A')+26] += 1
            # key = ''.join([str(count) for count in counts])
            result[tuple(counts)].append(s)
        
        return list(result.values())



