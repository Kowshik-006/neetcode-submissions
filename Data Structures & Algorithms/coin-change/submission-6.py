class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        seen = [False] * (amount+1)
        seen[0] = True
        q = deque([0])
        res = 0

        while q:
            res += 1
            lenq = len(q)
            """
            for going level by level
            the code inside the outer loop below takes one level
            then generates the next level
            we want to only pop the elements of the current level in one iteration
            otherwise the res value will increment when popping 
            elements of the current level
            """
            for _ in range(lenq):
                curr = q.popleft()
                for coin in coins:
                    nxt = curr + coin
                    if nxt == amount:
                        return res
                    if nxt > amount or seen[nxt]:
                        continue
                    
                    seen[nxt] = True
                    q.append(nxt)

        return -1