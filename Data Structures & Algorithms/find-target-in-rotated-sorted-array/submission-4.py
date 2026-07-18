class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        mid = l

        def binSearch(left, right):
            while left <= right:
                m = (left + right) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    left = m + 1
                else:
                    right = m - 1
            return -1
        res = binSearch(0, mid - 1)
        return res if res != -1 else  binSearch(mid, len(nums) - 1)

        