# https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/262/
"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeroes = len(list(filter(lambda x: x == 0, nums)))
        if zeroes == 0:
            return
        n = len(nums)
        # all zeroes at end only
        if all(x == 0 for x in nums[n-zeroes:]):
            return
        
        # cur_write, cur = n - 1, 0
        # move zeroes to end, only need to check n - zeroes numbers.
        # while cur < n - zeroes:
        #     if nums[cur] == 0:
        #         nums[cur], nums[cur_write] = nums[cur_write], nums[cur]
        #         cur_write -= 1
        #     else:
        #         cur += 1
        """
        [0,1,0,3,12]
        cur = 0, cur_write = 0, inc cur
        cur = 1, do swap [1,0,0,3,12], cur_write = 1, inc cur
        [1,0,0,3,12]
        cur = 2, nothing, increment cur
        cur = 3, do swap [1,3,0,0,12], cur_write = 2, inc cur
        cur = 4, do swap [1,3,12,0,0], cur_write = 3, inc cur
        """
        # used as a value to indicate unset.
        # earlier I used None but then distinguishing between cur_write = 0 and None is annoying.
        cur_write = -1
        
        cur = 0
        while cur < n:
            if nums[cur] == 0 and cur_write == -1:
                cur_write = cur
                cur += 1
            elif nums[cur] != 0 and cur_write != -1:
                # do a swap bringing the zero to cur pos.
                nums[cur], nums[cur_write] = nums[cur_write], nums[cur]
                cur_write = cur_write + 1
                cur += 1
            else:
                cur += 1
        
