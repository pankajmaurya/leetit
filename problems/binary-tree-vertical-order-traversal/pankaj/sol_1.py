from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        l2r = defaultdict(list)
        t2b = {}
        
        # node is at x = hpos, y = vpos
        def fill(node, hpos, vpos):
            l2r[hpos].append(node)
            t2b[node] = vpos
            
            if node.left:
                fill(node.left, hpos-1, vpos+1)
            if node.right:
                fill(node.right, hpos+1, vpos+1)
        
        fill(root, 0, 0)
        
        out = []
        for k in sorted(l2r.keys()):
            # if len(l2r[k]) == 1:
            #     out.append([l2r[k][0].val])
            # else:
            out.append(list(map(lambda p: p[1], sorted(map(lambda n: (t2b[n], n.val), l2r[k]), key = lambda p: p[0]))))
                
        return out
