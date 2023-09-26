from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        d = defaultdict(int)
        l, r = 0, 0
        
        ans = -1
        while l < n and r <= n:
            if len(filter(lambda x: x, [d[i] > 0 for i in d])) <= k:
                if r - l > ans:
                    ans = r - l
                # expand sliding window
                r += 1
                if r <= n:
                    d[s[r-1]] += 1
            else:
                # we have to shrink
                d[s[l]] -= 1
                l += 1
        return ans
