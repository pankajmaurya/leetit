from collections import defaultdict
import pdb
class Solution(object):
    def canJump(self, a):
        """
        :type a: List[int]
        :rtype: bool
        """
        n = len(a)
        if n == 1:
            return True
        b = []
        for i, x in enumerate(a):
            b.append(i + int(x))
        if max(b) < n - 1:
            return False
        dpsolve={}
        dpsolve[(n-1, n-1)] = True
        
        def solve(start, end):
            #pdb.set_trace()
            
            #print('solving for ', start, end)
            while start < n-1 and a[start] == 1:
                start = start + 1
            if (start, end) in dpsolve:
                return dpsolve[(start, end)]
            if start >= end:
                return True
            if a[start] == 0:
                return False
            if a[start] >= end - start:
                return True
            # where is the max reach from start + 1: a[start] cannot be zero?
            reaches = []
            for step in range(a[start], 0, -1):
                reaches.append(start + a[start+step] + step)
            reaches = set(reaches)
            #print(reaches)
            maxreach = max(reaches)
            #print('maxreach is ', maxreach)
            #pdb.set_trace()
            return any([solve(next_start, end) for next_start in range(maxreach,start,-1)])
            
        return solve(0, n-1)            
               
        
      
        
            
                
        
