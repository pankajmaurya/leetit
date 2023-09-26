# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
    
        def helper(node, depth):
            """
            return the max depth in the subtree rooted at node and the diameter
            of the subtree rooted at the given node.
            """
            max_left_depth = -1
            max_right_depth = -1
            max_left_diameter = -1
            max_right_diameter = -1
            
            if node.left:
                max_left_depth, max_left_diameter = helper(node.left, depth+1)
                
            if node.right:
                max_right_depth, max_right_diameter = helper(node.right, depth+1)
                
            diameter_via_node = 0
            if max_left_depth >= 0 and max_right_depth >= 0:
                diameter_via_node = max_left_depth + max_right_depth - 2 * depth
            elif max_left_depth >= 0:
                diameter_via_node = max_left_depth
            elif max_right_depth >= 0:
                diameter_via_node = max_right_depth
            else:
                diameter_via_node = 0
            #print('helper for ', node.val, max_left_depth, max_right_depth, depth, max_left_diameter, max_right_diameter, diameter_via_node)
            return max(max_left_depth, max_right_depth, depth), max(max_left_diameter, max_right_diameter, diameter_via_node)
                
        maxdepth, diameter = helper(root, 0)
        return diameter
