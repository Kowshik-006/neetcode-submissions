"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        def bfs():
            nonlocal node
            q = deque()
            vis_map = {}
            root = Node(node.val)
            q.append(node)
            vis_map[node.val] = root

            while q:
                node = q.popleft()
                new_node = vis_map[node.val]

                for nb in node.neighbors:
                    if nb.val not in vis_map:
                        n_nb = Node(nb.val)
                        vis_map[nb.val] = n_nb
                        q.append(nb)
                    else:
                        n_nb = vis_map[nb.val]

                    new_node.neighbors.append(n_nb)
            return root

        return bfs()
                    
                        
        
