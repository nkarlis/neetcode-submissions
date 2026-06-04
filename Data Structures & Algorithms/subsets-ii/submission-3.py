class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        stack = []

        def dfs(i):
            if len(nums) == i:
                res.append(stack.copy())
                return
            stack.append(nums[i])
            dfs(i+1)
            stack.pop()
            while i+1<len(nums) and nums[i+1] == nums[i]:
                i+=1
            dfs(i+1)
        
        dfs(0)
        return res