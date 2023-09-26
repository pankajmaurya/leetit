# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        
        def allInRange(node, l, u):
            if not node: return True
            print('checking for node with value: ', node.val, 'with l, u: ', l, u)
            if u != None and node.val >= u: return False
            if l != None and node.val <= l: return False
            return allInRange(node.left, l, node.val) and allInRange(node.right, node.val, u)
        
        return allInRange(root.left, None, root.val) and allInRange(root.right, root.val, None)
