import math

class Solution(object):
    def myPow(self, x, n):
        
        if n == 0: return 1
        if n == 1: return x
        
        # n is a 32 bit signed number.
        absn = abs(n)
        
        # how many bits does absn have?
        bits = int(math.ceil(math.log(absn, 2)))
        
        # keep powers of x to k where k = 2 ^ i
        powers = {}
        powers[1] = x
        # x ^ 1 = x
        # x ^ 2 = (x ^ 1) * (x ^ 1) # i = 1
        # x ^ 4 = (x ^ 2) * (x ^ 2) # i = 2
        
        for i in range(1, bits+1):
            k = 1 << i
            prev = 1 << (i-1)
            powers[k] = powers[prev] * powers[prev]
            
        res = 1
        for key in sorted(powers.keys(), reverse=True):
            if absn >= key:
                absn -= key
                res *= powers[key]
                
        if n < 0:
            return 1 / res
        else:
            return res
