class Solution(object):
    def __init__(self):
        self.dp = {}
        
    def checkIsMatch(self, s, p):
        if (s, p) in self.dp:
            return self.dp[(s, p)]
        else:
            ans = self.isMatch(s, p)
            self.dp[(s, p)] = ans
            return ans
        
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(s) == 0 and len(p) == 0:
            return True
        
        if len(s) > 0 and len(p) == 0:
            return False
        
        # either len(s) == 0 and len(p) > 0 OR both lengths > 0 cases remain.
        firstMatch = (len(s) > 0 and p[0] in {'.', s[0]})
        
        # is 2nd position in p = *
        if len(p) > 1 and p[1] == '*':
            # zero or more matches of s[0]
            zeroMatches = self.checkIsMatch(s, p[2:])
            
            
            oneOrMoreMatches = firstMatch and self.checkIsMatch(s[1:], p)
            
            return zeroMatches or oneOrMoreMatches
        # first match and match of rest
        else: 
            return firstMatch and self.checkIsMatch(s[1:], p[1:])
