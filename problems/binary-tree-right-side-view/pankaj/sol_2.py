# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def helper(current_level, prev_right_view):
            """
            We are going to get called initially with [[root], []]

            We can simply think of doing a level traversal and picking out
            the rightmost of each level
            """
            # create a local right view and initialize it by copy over all of prev_right_view
            local_right_view=[]
            for n in prev_right_view:
                local_right_view.append(n)

            # select the right most member of the current_level
            if len(current_level) > 0:
                local_right_view.append(current_level[-1].val)
            else:
                return local_right_view

            # compute next_level from current_level
            next_level = []
            for n in current_level:
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
            
            # call the helper with next_level and the local_right_view
            return helper(next_level, local_right_view)

        if root is None:
            return []
        ans = helper([root], [])
        return ans
        
