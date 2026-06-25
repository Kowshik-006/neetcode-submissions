class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for dst, src in prerequisites:
            indeg[dst] += 1
            adj[src].append(dst)

        q = deque()

        for c in range(numCourses):
            if indeg[c] == 0:
                q.append(c)
        
        finished = 0
        
        while q:
            c = q.popleft()
            finished += 1

            for nei in adj[c]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)

        return finished == numCourses