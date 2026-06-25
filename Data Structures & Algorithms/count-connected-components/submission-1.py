class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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
        for node in range(n):
            if node not in visited:
                traverse(node)
                components += 1
        
        return components