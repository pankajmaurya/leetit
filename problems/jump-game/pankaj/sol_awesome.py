# This is not by me but I wanted to look at others work as I was doing so bad in my attempts.
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        goal = len(nums) - 1  # Start from the last index
        for i in range(len(nums) - 2, -1, -1):  # Traverse from right to left
            if i + nums[i] >= goal:
                goal = i  # Move the goalpost to the current index
        return goal == 0  