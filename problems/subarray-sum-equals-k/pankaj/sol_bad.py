from collections import defaultdict
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        We temporarily refer to indices as 1 index based.

        Pi = sum of prefix array upto i, with P0 = 0

        P1 = nums[0]
        P2 = nums[0]+ nums[1]
        ...

        Pn = sum of all nums
        keep a dictionary
        d[sum] = count of ways which produce that sum

        With this, for a given Pj j > 0, Pj - Pi is a subarray sum.
        Hence we may look for a Pi with value Pj - k
        """
        n = len(nums)
        d = defaultdict(int)
        d[0] = 1 # for P0 = 0
        p_i = 0
        ways  = 0
        for i in range(1, n+1):
            p_i += nums[i - 1]
            print(f"p_i is {p_i}")
            ways += d[p_i - k]
            d[p_i] += 1

        
        return ways

s = Solution()
print(s.subarraySum([1], 0))


        