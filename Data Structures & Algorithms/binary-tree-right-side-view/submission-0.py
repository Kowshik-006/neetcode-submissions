# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
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
        
        result = []

        for level in levels:
            result.append(level[-1].val)
        
        return result