class Solution(object):
    def findMinIndex(self, a):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(a)
        if n == 1:
            return 0
        
        l, u = 0, n-1
        
        while l < u:
            m = l + (u - l) / 2
            # print(l, m, u)
            if a[l] < a[u]:
                return l
            else:
                if a[l] <= a[m]:
                    l = m + 1
                else:
                    u = m
        return l
    
    def search(self, a, t):
        n = len(a)
        if n == 1:
            return 0 if t == a[0] else -1
        
        if n == 0:
            return -1
        
        minIndex = self.findMinIndex(a)
        
        if minIndex == 0:
            l, u = 0, n-1
        else:
            l1,u1 = 0, minIndex-1
            l2,u2 = minIndex, n-1
            
            if a[l1] <= t <= a[u1]:
                l,u = l1,u1
            else:
                l,u = l2,u2
        
        while l <= u:
            m = l + (u - l)/ 2
            if a[m] == t:
                return m
            elif a[m] > t:
                u = m - 1
            else:
                l = m + 1
        return -1
