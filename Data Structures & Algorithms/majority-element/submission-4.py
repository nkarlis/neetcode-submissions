class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxEl, maxCount = nums[0], 0
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            if count[num] > maxCount:
                maxCount = count[num]
                maxEl = num
        return maxEl