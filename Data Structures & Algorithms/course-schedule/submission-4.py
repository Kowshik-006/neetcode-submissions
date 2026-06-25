class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {}
        for c in range(numCourses):
            pre_map[c] = set()
        for c, p in prerequisites:
            pre_map[c].add(p)

        def hasCycle(c, visited):
            if len(pre_map[c]) == 0:
                return False
            if c in visited:
                return True
            for p in pre_map[c]:
                if hasCycle(p,visited.union({c})):
                    return True
            return False
        
        for c in range(numCourses):
            visited = set()
            if hasCycle(c,visited):
                # print(c)
                return False

        return True
