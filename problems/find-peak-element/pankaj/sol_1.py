class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        if n == 0: return -1
        if n == 1: return 0
        
        l, u = 0, n-1
        while l < u:
            m = l + (u - l) / 2
            # we can assume nums[-1] = nums[n] = float('-inf')
            if nums[m] > nums[m+1]:
                # a peak should be on the left side
                u = m
            else:
                l = m + 1
            
        return l
