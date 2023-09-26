from collections import defaultdict
import copy
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        i = 0 to len(coins)
        j = 0 to amount
        
                0    1     2    3    4     5
        []      1    0     0    0    0     0
        [1]     1   1+0=1  
        [1,2]   1 
        [1,2,5] 1 
        """
        coins.sort()
        
        dp = {}
        # Making amount 0
        for i in range(len(coins) + 1):
            dp[(i, 0)] = 1
        
        # Making any non zero amount with zero coins
        for j in range(1, amount+1):
            dp[(0, j)] = 0
            
        # fill table row by row
        for i in range(1, len(coins)+1):
            for cur_amount in range(1, amount+1):
                c = coins[i-1]
                ways1, ways2 = 0, 0
                if c <= cur_amount:
                    ways1 = dp[(i, cur_amount - c)]
                ways2 = dp[(i-1, cur_amount)]
                dp[(i, cur_amount)] = ways1 + ways2
                
        return dp[(len(coins), amount)]
