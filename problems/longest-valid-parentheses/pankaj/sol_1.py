from collections import defaultdict
class Solution(object):
    def longestValidParentheses(self, s):
        start, maxlen = 0, 0
        stack = []
        for index, cc in enumerate(s):
            if cc == "(":
                stack.append(index)
            else:
                if len(stack) != 0:
                    stack.pop()
                    if len(stack) != 0:
                        maxlen = max(maxlen, index - stack[-1])
                    else:
                        maxlen = max(maxlen, index - start +1 )
                else:
                    start = index + 1
        
        return maxlen
                    
                
        
            
