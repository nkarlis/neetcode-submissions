class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minP = prices[0]
        for p in prices:
            minP = min(minP, p)
            profit = max(p - minP, profit)
        return profit