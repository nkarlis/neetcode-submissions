class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = prices[0]
        res = 0
        for p in prices:
            minP = min(minP, p)
            res = max(res, p - minP)
        return res