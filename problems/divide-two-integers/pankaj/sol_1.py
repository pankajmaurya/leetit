class Solution(object):
    def divide(self, dividend, divisor):
        x = dividend < 0
        y = divisor < 0
        
        sign = x ^ y
        dividend = abs(dividend)
        divisor = abs(divisor)
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        
        starting with power = 31...0, each time see if 2^power * y < x, 
            if yes update x and result
        """
        result, power = 0, 31
        t = divisor << power
        while divisor <= dividend and power >= 0:
            # Finding largest value of power such that 2 ^ power * divisor < dividend
            while t > dividend and power > 0:
                power -= 1
                t >>= 1
            # print('updating result: ', dividend, divisor, power, t)
            result += (1 << power)
            dividend -= t
            
        # print('remainder is ', dividend)
        z = result * -1 if sign else result
        return max(-2147483648, min(z, 2147483647))
            
