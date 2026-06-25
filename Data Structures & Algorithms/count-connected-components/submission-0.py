class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        vertices = set()
        for i in range(n):
            vertices.add(i)
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def traverse(node):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    traverse(nei)
        components = 0
        while vertices:
            visited = set()
            node = vertices.pop()
            traverse(node)
            components += 1
            vertices -= visited
        
        return components