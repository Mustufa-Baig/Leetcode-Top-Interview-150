# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.rightView(root, result, 0)
        return result
    
    def rightView(self, curr, result, currDepth):
        if curr is None:
            return
        if currDepth == len(result):
            result.append(curr.val)
        self.rightView(curr.right, result, currDepth + 1)
        self.rightView(curr.left, result, currDepth + 1)