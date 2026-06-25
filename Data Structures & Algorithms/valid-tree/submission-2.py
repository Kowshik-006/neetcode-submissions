class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj = [[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def isAcyclic(node, parent):
            if node in visited:
                return False
            
            visited.add(node)

            for nei in adj[node]:
                if nei != parent:
                    if not isAcyclic(nei, node):
                        return False
            
            return True
        
        acyclic = isAcyclic(0,-1)
        connected = (len(visited) == n)

        return acyclic and connected


