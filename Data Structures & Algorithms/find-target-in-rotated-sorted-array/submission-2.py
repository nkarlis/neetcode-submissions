class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (r + l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        def binSearch(left, right):
            res = -1
            while left <= right:
                m = (right + left) // 2
                if nums[m] == target:
                    return m
                elif nums[m] > target:
                    right = m -1
                else:
                    left = m + 1
            return -1
        pos = l
        res = binSearch(0, pos - 1)
        return res if res != -1 else binSearch(pos, len(nums) - 1)
        

        