class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = defaultdict(int)

        for num in nums:
            num_count[num] += 1
        
        freq_buckets = [[] for i in range(len(nums)+1)]

        for num, count in num_count.items():
            freq_buckets[count].append(num)
        
        result = []

        for i in range(len(freq_buckets)-1, 0, -1):
            for num in freq_buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
