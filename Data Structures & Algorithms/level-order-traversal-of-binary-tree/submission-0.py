# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levels = [[root]]
        
        i = 0

        while True:
            level = []
            for node in levels[i]:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)

            if len(level) == 0:
                break
            
            levels.append(level)
            i += 1
        
        for level in levels:
            for i in range(len(level)):
                level[i] = level[i].val

        return levels