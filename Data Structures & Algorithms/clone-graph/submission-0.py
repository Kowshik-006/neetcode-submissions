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

        def bfs(new_node):
            nonlocal node
            q1 = deque()
            q2 = deque()
            vis_map = {}
            new_node.val = node.val
            q1.append(node)
            q2.append(new_node)
            vis_map[new_node.val] = new_node

            while q1:
                node = q1.popleft()
                new_node = q2.popleft()

                for nb in node.neighbors:
                    if nb.val not in vis_map:
                        n_nb = Node(nb.val)
                        vis_map[nb.val] = n_nb
                        q1.append(nb)
                        q2.append(n_nb)
                    else:
                        n_nb = vis_map[nb.val]

                    new_node.neighbors.append(n_nb)
        
        new_node = Node()
        bfs(new_node)

        return new_node
                    
                        
        
