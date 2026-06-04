class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for p in prices:
            minBuy = min(p, minBuy)

            maxP = max(maxP, p-minBuy)


        return maxP