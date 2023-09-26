# https://leetcode.com/explore/interview/card/facebook/5/array-and-strings/263/
# https://leetcode.com/problems/add-binary/

"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.
"""
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        na, nb = len(a), len(b)
        
        if na != nb:
            if na < nb:
                a = '0' * (nb - na) + a
            else:
                b = '0' * (na - nb) + b
                
        na, nb, n = len(a), len(b), len(a)
        assert(na == nb)
        
        o = ""
        c = 0

        for i in range(n):
            s = int(a[n - 1 - i]) + c + int(b[n - 1 - i])
            o = str(bin(s)[-1]) + o
            if s <= 1:
                c = 0
            else:
                c = 1
        if c > 0:
            o = str(c) + o
            
        return o
