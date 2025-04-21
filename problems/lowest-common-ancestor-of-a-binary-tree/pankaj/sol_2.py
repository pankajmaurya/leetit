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
        def inSubtree(root, node):
            if root == None or node == None:
                return False
            if root == node:
                return True
            return inSubtree(root.left, node) or inSubtree(root.right, node)

        def lcaHelper(root, p, q):
            if not root:
                return None

            if root == p and inSubtree(p, q):
                return p

            if root == q and inSubtree(q, p):
                return q

            lans, rans = None, None
            if root.left:
                lans = lcaHelper(root.left, p, q)

            if lans:
                return lans

            if root.right:
                rans = lcaHelper(root.right, p, q)

            if rans:
                return rans

            if inSubtree(root.left, p) and inSubtree(root.right, q) or inSubtree(root.left, q) and inSubtree(root.right, p):
                return root

            return None

        return lcaHelper(root, p, q)

