import bisect

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        
        # which row may contain the target?
        first_col = []
        for i in range(m):
            first_col.append(matrix[i][0])
            
        # Find the position such that all values from that to right are strictly larger than target.
        row = bisect.bisect_right(first_col, target)
        
        row_to_search = row - 1
        
        pos = bisect.bisect_left(matrix[row_to_search], target)
        
        if pos == n:
            return False
        return matrix[row_to_search][pos] == target
