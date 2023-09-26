# https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/3013/   

from collections import deque
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        table = [[0,0,0,0,0,0,0,0,0,0],
                 [0,1,2,3,4,5,6,7,8,9],
                 [0,2,4,6,8,10,12,14,16,18],
                 [0,3,6,9,12,15,18,21,24,27],
                 [0,4,8,12,16,20,24,28,32,36],
                 [0,5,10,15,20,25,30,35,40,45],
                 [0,6,12,18,24,30,36,42,48,54],
                 [0,7,14,21,28,35,42,49,56,63],
                 [0,8,16,24,32,40,48,56,64,72],
                 [0,9,18,27,36,45,54,63,72,81]]
        l1, l2 = len(num1), len(num2)
        
        l = min(l1, l2)
        nsmall = num1 if l == l1 else num2
        nlarge = num2 if l == l1 else num1
        # print(nsmall, nlarge)
        
        def multByDigit(a, d):
            carry = 0
            ans = deque()
            for c in a[::-1]:
                x = table[int(c)][int(d)] + carry
                ans.appendleft(str(x % 10))
                carry = x / 10
            
            if carry:
                ans.appendleft(str(carry))
            return ''.join(ans)
            
        def multByPower10(a, power):
            return a + '0' * power
        
        power = 0
        values = []
        for d in nsmall[::-1]:
            values.append(multByPower10(multByDigit(nlarge, d), power))
            power += 1
        return str(sum(map(int, values)))

