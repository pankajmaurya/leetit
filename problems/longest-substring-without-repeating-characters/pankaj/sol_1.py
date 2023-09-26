from collections import OrderedDict
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
            
        maxlen = 0
        curstr = ""
        for i, c in enumerate(s):
            if c not in curstr:
                curstr = curstr + c
                maxlen = max(maxlen, len(curstr))     
            else:
                pos = curstr.find(c)
                if pos == len(curstr):
                    curstr = ""
                else:
                    curstr = curstr[pos+1:]
                curstr = curstr + c
                maxlen = max(maxlen, len(curstr))
                
        maxlen = max(maxlen, len(curstr))
        return maxlen
