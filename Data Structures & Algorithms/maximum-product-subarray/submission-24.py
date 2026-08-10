class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin, res = 1, 1, nums[0]
        for num in nums:
            temp = curMax * num
            curMax = max(curMax * num, curMin * num, num)
            curMin = min(temp, curMin * num, num)
            res = max(res, curMax)
        return res