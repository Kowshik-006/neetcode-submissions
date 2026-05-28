class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = defaultdict(list)

        for s in strs:
            str_dict[tuple(sorted(s))].append(s)
        
        result = []

        for key, value in str_dict.items():
            result.append(value)

        return result