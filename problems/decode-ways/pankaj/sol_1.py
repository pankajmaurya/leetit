class Solution(object):
    def __init__(self):
        self.dp = {}
        
    def ndhelper(self, s):
        if s in self.dp:
            return self.dp[s]
        else:
            ans = self.nd(s)
            self.dp[s] = ans
            return ans
        
    def nd(self, s):
        if len(s) == 0:
            return 1
        if len(s) == 1:
            if int(s) > 0 and int(s) < 27:
                return 1
            else:
                return 0
        
        # if len(s) == 0:
            # return 1
        # At every step we can take one or two chars if the two chars <= 26
        
        ways1, ways2 = 0, 0
        # print('>>>>', s)
        if int(s[0]) != 0:
            suffix_len_after_one_char = len(s[1:])
            if suffix_len_after_one_char > 0:
                ways1 = self.ndhelper(s[1:])
            else:
                ways1 = 1
            # print(s[0], s, ways1)
        else:
            return 0
        
        if 0 < int(s[0:2]) <= 26:
            ways2 = self.ndhelper(s[2:])
            # print(s[0:2], s, ways2)
            
        return ways1 + ways2
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        else:
            return self.ndhelper(s)
        
        
