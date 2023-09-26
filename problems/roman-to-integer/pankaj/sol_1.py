https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/3010/
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        d['I'] = 1
        d['IV'] = 4
        d['V'] = 5
        d['IX'] = 9
        d['X'] = 10
        d['XL'] = 40
        d['L'] = 50
        d['XC'] = 90
        d['C'] = 100
        d['CD'] = 400
        d['D'] = 500
        d['CM'] = 900
        d['M'] = 1000
        
        stack = []
        
        pos = 0
        n = len(s)
        acc = 0
        # s = "CDLXXII", n = 7
        # pos = 0
        
        # 6 < 7
        while pos < n: 
            if pos + 2 <= n and s[pos:pos+2] in d:
                # acc += 400 : acc = 400
                acc += d[s[pos:pos+2]]
                # pos = 2
                pos = pos + 2
            # 7 <= 7
            elif pos + 1 <= n and s[pos:pos+1] in d:
                # acc += 1, acc = 472
                acc += d[s[pos:pos+1]]
                # pos = 7
                pos = pos + 1
        return acc
            

