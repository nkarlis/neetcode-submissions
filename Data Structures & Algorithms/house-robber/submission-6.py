class Solution:
    def rob(self, nums: List[int]) -> int:
        r1, r2 = 0, 0
        for num in nums:
            newRob = max(r1 + num, r2)
            r1 = r2
            r2 = newRob
        return r2