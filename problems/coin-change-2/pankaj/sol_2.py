class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        ways = {}
        coins = sorted(coins)
        numCoins = len(coins)
        # ways is indexed by a tuple of (numCoins, amount)
        # ways[(i, 0)] = 1 for i in range(1,numCoins+1)
        for i in range(1, numCoins+1):
            ways[(i, 0)] = 1
        
        # there are zero ways to make a non zero amount with zero coins.
        for a in range(1, amount+1):
            ways[(0, a)] = 0

        for a in range(1, amount+1):
            for c in range(1, numCoins+1):
                # start filling row wise top to bottom.
                # last coin included is coins[c - 1]
                max_denomination = coins[c - 1]
                if a >= max_denomination:
                    ways[(c, a)] = ways[(c, a - max_denomination)] + ways[(c - 1, a)]
                else:
                    ways[(c, a)] = ways[(c - 1, a)]

        return ways[(numCoins, amount)]
