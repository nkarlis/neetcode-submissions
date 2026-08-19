class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res, maxEl = 0, 0
        for n in nums:
            count[n] += 1
            if count[n] > res:
                res = count[n]
                maxEl = n
        return maxEl
