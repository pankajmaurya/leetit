class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        prices = [7,1,5,3,6,4]
        profit = selling price - purchasing price (aka buying price)
        max profit if sold on day i = price on day i - min buying price seen so far
        
        max profit = max(profit on day i) For all i
        
        """
        max_profit = 0
        if len(prices) <= 1:
            return max_profit
        
        # atleast 2 prices
        min_so_far = prices[0]
        
        for p in prices[1:]:
            min_so_far = min(min_so_far, p)
            if min_so_far != p:
                max_profit = max(max_profit, p - min_so_far)
        return max_profit
        
