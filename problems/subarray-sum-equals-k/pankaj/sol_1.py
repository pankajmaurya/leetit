# https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/3019/
from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        c = 0
        n = len(nums)
        d = defaultdict(int)
        sum_until = 0
        # d will store number of ways we have seen so far of getting subarray sum i
        d[0] = 1
        
        for v in nums:
            sum_until += v
            c += d[sum_until - k]
            d[sum_until] += 1
            
        return c
