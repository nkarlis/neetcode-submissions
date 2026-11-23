class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        target = s // 2
        dp = set()
        dp.add(0)
        for i in range(len(nums)):
            nextDP =  set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t)
                nextDP.add(t + nums[i])
            dp = nextDP
        return False