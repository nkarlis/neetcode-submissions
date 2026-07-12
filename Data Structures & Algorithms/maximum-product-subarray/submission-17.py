class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, curMax, curMin = nums[0], 1, 1
        for num in nums:
            tmp = num * curMax
            curMax = max(num, curMax * num, curMin * num)
            curMin = min(num, tmp, curMin * num)
            res = max(res, curMax)
        return res