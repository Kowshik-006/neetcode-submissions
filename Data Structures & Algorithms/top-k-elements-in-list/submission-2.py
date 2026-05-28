class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1

        keys = sorted(hashmap, key = lambda i : hashmap[i], reverse = True)

        if len(keys) < k:
            return keys
        else:
            return keys[:k]




