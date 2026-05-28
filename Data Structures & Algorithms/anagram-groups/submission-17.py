class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = defaultdict(list)
        
        for s in strs:
            # Store the character count in each string
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            str_dict[tuple(count)].append(s)
        
        return list(str_dict.values())
