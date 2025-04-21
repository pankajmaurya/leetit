# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(node: TreeNode, depth: int) -> (float, float):
            ldia, rdia = float("-inf"), float("-inf")
            ldepth, rdepth = depth, depth

            if node.left is None and node.right is None:
                return 0, depth

            if node.left is not None:
                ldia, ldepth = helper(node.left, depth+1)
            if node.right:
                rdia, rdepth = helper(node.right, depth+1)

            # max of ldia, rdia, but what about case when it passes through node?
            return max(ldia, rdia, ldepth + rdepth - 2 * depth), max(ldepth, rdepth)
        

        if root is None:
            return 0
        dia, depth = helper(root, 0)
        return dia
            
        
