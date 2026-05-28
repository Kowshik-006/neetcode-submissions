from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        mid = 1
        right = max(piles)
        result = 1

        while left <= right:
            mid = (left+right) // 2
            time = 0
            for pile in piles:
                time += ceil(pile / mid)

            if time <= h:
                # valid result
                # let's see if the rate can be decreased further
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        print(ceil(5/2))
        print(ceil(float(5)/2))
        return result