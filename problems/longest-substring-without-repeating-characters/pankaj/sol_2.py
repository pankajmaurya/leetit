from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        
        d = defaultdict(list)
        for i, ch in enumerate(s):
            d[ch].append(i)
            
        print d
        """
        l = 0
        maxl = 0
        u = {}
        for i, ch in enumerate(s):
            if ch not in u:
                u[ch] = i
                l +=1
                maxl=max(l, maxl)
                #print("case1: ", i, ch, maxl, u)
            else:
                old = u[ch]
                l = i - old
                maxl=max(l, maxl)
                oldkeys = u.keys()
                for k in oldkeys:
                    if u[k] <= old:
                 #       print('deleting', k, u[k])
                        del(u[k])
                u[ch] = i
                #print("case2: ", i, ch, old, maxl, u)
        
        return maxl
