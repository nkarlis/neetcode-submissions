class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        curMin, curMax = 1, 1

        for n in nums:
            tmp1 = curMax * n
            tmp2 = curMin *n
            curMax = max(tmp1, tmp2, n)
            curMin = min(tmp1, tmp2, n)
            res = max(res, curMax)
        return res
