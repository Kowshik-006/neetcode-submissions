class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [[] for _ in range(n+1)]
        result = []

        mp = {}

        for num in nums:
            mp[num] = mp.get(num,0) + 1

        for num, cnt in mp.items():
            buckets[cnt].append(num)

        for i in range(n, 0, -1):
            for num in buckets[i]:
                if k > 0:
                    result.append(num)
                    k -= 1
                else:
                    break
        return result