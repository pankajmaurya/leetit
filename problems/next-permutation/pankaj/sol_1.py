# https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/3012/
class Solution(object):
    def nextPermutation(self, a):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(a)
        if n <= 1:
            return
        
        # Find largest pos such that item after it is larger than at pos.
        # For a in descending order, no such pos can be found. (sort hence)
        pos = -1
        for i in range(n-1, 0, -1):
            if a[i-1] < a[i]:
                pos = i-1
                break

        if pos == -1:
            a.sort()
            return
        
        assert(pos != -1)
       # 2 2 2 4 7 6 3 1 -> 2 2 2 6 1 3 4 7
       #           ^
       #           |
       #       nextpos
        nextpos = n-1
        for i in range(n-1, pos, -1):
            if a[i] > a[pos]:
                nextpos = i
                break
                
        a[pos],a[nextpos] = a[nextpos],a[pos]
        start = pos+1
        end = n-1
        # reverse this.
        while start < end:
            a[start], a[end] = a[end], a[start]
            start += 1
            end -= 1
            

