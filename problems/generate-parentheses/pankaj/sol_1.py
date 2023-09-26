class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        
        if n == 1:
            return ['()']
        
        assert(n > 1)
        
        def gen(remain_l, remain_r, prefix = '', out=[]):
            if remain_r == 0:
                out.append(prefix)
            else:
                if remain_l > 0:
                    gen(remain_l-1, remain_r, prefix + '(', out)
                if remain_r > remain_l and remain_r > 0:
                    gen(remain_l, remain_r - 1, prefix + ')', out)
        
        out = []
        gen(n, n, '', out)
        
        return out
