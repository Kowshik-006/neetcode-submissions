class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        # Numbers in the array can have frequency from 0 to len(nums)
        # freq[1] stores elements having frequnecy = 1
        freq = [[] for i in range(len(nums)+1)]

        for num, cnt in hashmap.items():
            freq[cnt].append(num)
        
        result = []

        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result
