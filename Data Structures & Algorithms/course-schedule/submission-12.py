class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {}
        visited = set()

        for c in range(numCourses):
            pre_map[c] = []
        for c, p in prerequisites:
            pre_map[c].append(p)

        def hasCycle(c):
            if len(pre_map[c]) == 0:
                return False
            if c in visited:
                return True
            visited.add(c)
            for p in pre_map[c]:
                if hasCycle(p):
                    return True
            visited.remove(c)
            # No cycle can be found from this course
            # So, if we reach this course again, we need not check its prerequisites
            pre_map[c] = []
            return False
        
        for c in range(numCourses):
            if hasCycle(c):
                return False

        return True
