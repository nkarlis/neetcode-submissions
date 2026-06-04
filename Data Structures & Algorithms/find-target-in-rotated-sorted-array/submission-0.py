class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l+r)//2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m +1
        
        p = l

        def binSearch(l, r):
            while l <= r:
                m = (l+r)//2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    r = m-1
                else:
                    l = m+1
            return -1

        res = binSearch(0, p-1)
        if res != -1:
            return res
        return binSearch(p, len(nums) - 1)