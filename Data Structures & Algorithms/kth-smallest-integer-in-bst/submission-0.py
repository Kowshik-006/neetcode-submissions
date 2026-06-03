# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []

        def inOrder(root, values):
            if not root:
                return
            inOrder(root.left, values)
            values.append(root.val)
            inOrder(root.right, values)
        
        
        inOrder(root, values)

        return values[k-1]