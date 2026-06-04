class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        curMin, curMax = 1, 1

        for n in nums:
            tempmin =  curMin * n
            tempmax =   n*curMax  
            curMin = min(tempmin, tempmax, n)
            curMax = max(tempmax, tempmin, n)
            res = max(res, curMax)

        return res
