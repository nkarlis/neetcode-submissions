class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # default value, can't be zero due to negatives
        res = nums[0]
        total = 0

        for n in nums:
            total += n
            res = max(res, total)
            if total < 0:
                total = 0
        return res
