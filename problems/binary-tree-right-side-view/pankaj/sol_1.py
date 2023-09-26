# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        ans = []
        level = [root]
        while level:
            nextlevel = []
            ans.append(level[-1].val)
            for n in level:
                if n.left: nextlevel.append(n.left)
                if n.right: nextlevel.append(n.right)
            level = nextlevel
        return ans
