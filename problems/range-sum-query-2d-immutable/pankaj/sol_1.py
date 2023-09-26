class NumMatrix(object):

    def __init__(self, a):
        """
        :type matrix: List[List[int]]
        """
        self.a = a
        self.m = len(a)
        self.n = len(a[0]) if self.m > 0 else 0
        self.cum = [[0 for j in range(self.n)] for i in range(self.m)]
        for i in range(self.m):
            s = 0
            for j in range(self.n):
                s += self.a[i][j]
                self.cum[i][j] = s
        print(self.cum)
                
        
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        print('args are ', row1, col1, row2, col2)
        def getM(i, j):
            # sum of Matrix with 0,0 and i, j as diametrically opposite corners.
            if i == -1 or j == -1:
                return 0
            m = 0
            for row in range(i+1):
                m += self.cum[row][j]
            return m
        
        print('getM(row2, col2)', getM(row2, col2))
        print('getM(row1 - 1, col1 - 1)', getM(row1 - 1, col1 - 1))
        print('getM(row1 - 1, col2)', getM(row1 - 1, col2))
        print('getM(row2, col1 - 1)', getM(row2, col1 - 1))
        return getM(row2, col2) + getM(row1 - 1, col1 - 1) - getM(row1 - 1, col2) - getM(row2, col1 - 1)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
