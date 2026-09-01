class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin, res = 1, 1, nums[0]
        for n in nums:
            tmp = curMax * n
            curMax = max(tmp, curMin * n, n )
            curMin = min(tmp, curMin * n, n )
            res = max(res, curMax)
        return res