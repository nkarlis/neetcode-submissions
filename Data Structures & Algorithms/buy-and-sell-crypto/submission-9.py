class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minPrice = prices[0]

        for p in prices:
            minPrice = min(p, minPrice)
            maxP = max(maxP, p-minPrice)
        return maxP