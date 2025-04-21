class Solution:
    def search(self, a: List[int], target: int) -> int:
        """
        :type a: List[int]
        :type target: int
        :rtype: int
        """
        n = len(a)
        l, u = 0, n - 1

        if n == 1 and target == a[0]:
            return 0
        
        def getMinIndex():            
            l, u = 0, n - 1
            while l < u:
                if a[l] < a[u]:
                    return l
                m = int(l + (u - l) / 2)
                if a[m] >= a[l]:
                    # pivot is to the right of m
                    l = m + 1
                    print(f'{l}, {u} (pivot was to right of {m})')
                else:
                    # Note sometimes m can be same as l also
                    u = m
                    print(f'{l}, {u} (pivot was to left of {m})')
                
            return l

        x = getMinIndex()
        print(f'getMinIndex is {x}')

        if x == 0:
            l, u = 0, n - 1
        else:
            l1, u1 = 0, x - 1
            l2, u2 = x, n - 1
            l, u = None, None
            if a[l1] <= target and target <= a[u1]:
                l, u = l1, u1
            else:
                l, u = l2, u2

        print(f' searching in subarray a[{l}:{u}]')
        while l <= u:
            m = int(l + (u - l) / 2)
            print(f'In binary search {l}, {m}, {u}')
            if a[m] == target:
                return m
            elif a[m] > target:
                u = m - 1
            elif a[m] < target:
                l = m + 1
        
        return -1
