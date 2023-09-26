# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):    
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, u = 1, n
        ans = None
        while l <= u:
            m = l + (u - l) / 2
            if isBadVersion(m):
                ans = m
                u = m - 1
            else:
                l = m + 1
                
        return ans
