class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = defaultdict(int)

        for num in nums:
            num_count[num] += 1
        
        count_num = []

        for num, count in num_count.items():
            count_num.append([count, num])
        
        count_num.sort(reverse=True)

        result = []

        for i in range(k):
            result.append(count_num[i][1])

        return result