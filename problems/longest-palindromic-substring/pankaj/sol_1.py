from collections import defaultdict
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return s
        # default value is False
        # key would be tuple(i, j) i is starting index, j is end (exclusive)
        dp = defaultdict(bool)
        
        n = len(s)
        
        for i in range(n):
            dp[(i,i+1)] = True
        
        longest = s[0]
        longest_len = 1
        for window in range(2, n+1):
            for i in range(n):
                # start = i, end = i + window. end should be atmax n for a valid string.
                if i + window > n:
                    continue
                start = s[i]
                end = s[i+window-1]
                # print(si, sj)
                if start == end:
                    if window == 2 or dp[(i+1, i+window-1)]:
                        dp[(i,i+window)] = True
                        # update longest substring if we found a longer one.
                        if longest_len < window:
                            longest_len = window
                            longest = s[i:i+window]
        
        return longest
