class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        removals = []
        extras = {}
        for i, c in enumerate(s):
            if c == '(':
                stack.append(('(', i))
            elif c == ')':
                if len(stack) == 0:
                    removals.append((')', i))
                else:
                    stack.pop()
        while len(stack) != 0:
            removals.append(stack.pop())
        for r in removals:
            extras[r[1]] = True
        ans = []
        for i, c in enumerate(s):
            if i not in extras:
                ans.append(c)
        return ''.join(ans)
