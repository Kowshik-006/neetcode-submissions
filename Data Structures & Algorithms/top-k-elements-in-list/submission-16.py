class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = defaultdict(int)
        for num in nums:
            m[num] += 1

        buckets = [[] for i in range(len(nums)+1)]

        for num, count in m.items():
            buckets[count].append(num)

        result = []

        for count in range(len(buckets)-1,0,-1):
            for num in buckets[count]:
                result.append(num)
                k -= 1
                if k == 0:
                    return result
        