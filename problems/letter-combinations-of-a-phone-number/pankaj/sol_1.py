class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {}
        d['0'] = ' '
        d['1'] = ''
        d['2'] = 'abc'
        d['3'] = 'def'
        d['4'] = 'ghi'
        d['5'] = 'jkl'
        d['6'] = 'mno'
        d['7'] = 'pqrs'
        d['8'] = 'tuv'
        d['9'] = 'wxyz'
        
        n = len(digits)
        if n == 0:
            return []
        output = []
        
        # using backtracking
        # for i in range(len(digits)):
        current = []
        def appendOneLetter(i):
            if i == n:
                    output.append(''.join(current))
            else:
                for c in d[digits[i]]:
                    current.append(c)
                    appendOneLetter(i+1)
                    current.pop()
        
        appendOneLetter(0)                
                    
                
        
        
#         def directed_combos(index, sofar):
#             if index == len(digits):
#                 output.append(sofar)
#                 return
            
#             for c in d[digits[index]]:
#                 directed_combos(index+1, sofar + c)
                
#         directed_combos(0, "")
        
        return output
