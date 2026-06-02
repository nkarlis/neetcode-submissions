class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l)//2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        pos = l


        def binSearch(l, r):

            while l <= r:
                m = (l+r)//2
                if target == nums[m]:
                    return m
                elif target > nums[m]:
                    l= m+1
                else:
                    r = m-1
            return -1
        
        res = binSearch(0, pos-1)
        if res != -1:
            return res
        return binSearch(pos, len(nums) - 1)
