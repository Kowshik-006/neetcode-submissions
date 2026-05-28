class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = defaultdict(int)

        for num in nums:
            num_count[num] += 1
        
        count_num = []

        for num, count in num_count.items():
            count_num.append([count, num])
        # Sort in descending order based on the count
        count_num.sort(reverse=True)

        return [x[1] for x in count_num[:k]]