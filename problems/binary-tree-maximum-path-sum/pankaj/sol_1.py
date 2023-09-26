# Other tree problems to check
# https://leetcode.com/problemset/all/?search=binary%20tree%20max%20path
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        
        def getPathSumsForSubtree(node):
            # return 2 paths sums: one ending at the node, one anywhere in the subtree.
            if not node:
                return 0, 0
            
            p1l,p2l,p1r,p2r = float("-inf"), float("-inf"), float("-inf"), float("-inf")
            
            vnode = node.val
            if node.left:
                p1l, p2l = getPathSumsForSubtree(node.left)
            
            if node.right:
                p1r, p2r = getPathSumsForSubtree(node.right)
                
            p1 = max(p1l + vnode, p1r + vnode, vnode)
            p2 = max(p2l, p2r, p1l + vnode, vnode + p1r, p1l + vnode + p1r, vnode)
                        
            return p1, p2
        
        x, y = getPathSumsForSubtree(root)
        return y
