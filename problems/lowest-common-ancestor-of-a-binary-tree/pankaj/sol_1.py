# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if root == None or root.val == p.val or root.val == q.val:
            return root
        
        lans = self.lowestCommonAncestor(root.left, p, q)
        rans = self.lowestCommonAncestor(root.right, p, q)
        
        # lans, rans can be None if nodes are empty or non-empty if they match p or q.
        if lans and rans:
            return root
        else:
            # lans or rans must be None, the ans will be the other one
            if not lans:
                return rans
            else:
                return lans

            
        
