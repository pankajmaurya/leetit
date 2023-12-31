# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 2
#   \ 
#     1
#     p = 2, q = 1, root = 2
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        print(p.val, q.val, root.val)
        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root
        elif p.val <= root.val and q.val <= root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val >= root.val and q.val >= root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            raise Exception("illegal state: ", root.val, p.val, q.val)
    
        
