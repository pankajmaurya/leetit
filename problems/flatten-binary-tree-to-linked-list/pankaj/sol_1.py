# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        if not root: return root
        
        if not root.left and not root.right: return root
        
        lflat, rflat = self.flatten(root.left), self.flatten(root.right)            
        root.left = None
        
        cur = root
        if lflat:
            root.right = lflat
            while cur.right:
                cur = cur.right
        
        cur.right = rflat
            
        return root
        
